import numpy as np
import cv2
import os
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# ---------- CẤU HÌNH ----------
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
dataset_path = "./face_dataset/"
font = cv2.FONT_HERSHEY_SIMPLEX
THRESHOLD = 1000.0  # Ngưỡng khoảng cách để xác định "Unknown"

# ---------- TẢI DỮ LIỆU ----------
face_data = []
labels = []
names = {}
class_id = 0

for fx in os.listdir(dataset_path):
	if fx.endswith('.npy'):
		names[class_id] = fx[:-4]
		data_item = np.load(os.path.join(dataset_path, fx))
		face_data.append(data_item)
		target = class_id * np.ones((data_item.shape[0],))
		labels.append(target)
		class_id += 1

face_dataset = np.concatenate(face_data, axis=0)
face_labels = np.concatenate(labels, axis=0).reshape((-1, 1))

print("[INFO] Loaded training data:")
print("  Faces:", face_dataset.shape)
print("  Labels:", face_labels.shape)

# ---------- TIỀN XỬ LÝ ----------
scaler = StandardScaler()
face_dataset_scaled = scaler.fit_transform(face_dataset)

n_samples, n_features = face_dataset_scaled.shape
n_components = min(50, n_samples, n_features)  # Giới hạn số chiều PCA an toàn
pca = PCA(n_components=n_components)
face_dataset_pca = pca.fit_transform(face_dataset_scaled)

# ---------- HUẤN LUYỆN MÔ HÌNH ----------
knn_model = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn_model.fit(face_dataset_pca, face_labels.ravel())

# ---------- NHẬN DIỆN KHUÔN MẶT ----------
while True:
	ret, frame = cap.read()
	if not ret:
		continue

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x, y, w, h) in faces:
		offset = 5
		h_frame, w_frame = frame.shape[:2]

		# Giới hạn vùng cắt không vượt khung hình
		x1 = max(x - offset, 0)
		y1 = max(y - offset, 0)
		x2 = min(x + w + offset, w_frame)
		y2 = min(y + h + offset, h_frame)

		face_offset = frame[y1:y2, x1:x2]
		if face_offset.size == 0:
			continue

		face_section = cv2.resize(face_offset, (100, 100)).flatten().reshape(1, -1)

		# Chuẩn hóa và giảm chiều
		face_scaled = scaler.transform(face_section)
		face_pca = pca.transform(face_scaled)

		# Dự đoán
		pred_label = knn_model.predict(face_pca)[0]
		distances, _ = knn_model.kneighbors(face_pca, n_neighbors=1)
		min_dist = distances[0][0]

		# Xác định Unknown nếu khoảng cách quá xa
		if min_dist > THRESHOLD:
			pred_name = "Unknown"
			color = (0, 0, 255)  # Red
		else:
			pred_name = names[int(pred_label)]
			color = (0, 255, 0)  # Green

		# Hiển thị kết quả
		cv2.putText(frame, f"{pred_name}", (x, y - 10), font, 1, color, 2, cv2.LINE_AA)
		cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

	cv2.imshow("Face Recognition", frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
