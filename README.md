# Phronesis — Triage Hub `/remaining-questions`
> **Khóa học:** AI20K Batch 04 · Lớp 3A · Phòng E403  
> **Track:** B — Trợ lý Học viên (Discord) · **Đề bài:** B2 — Tính năng mới cho Đội ngũ Trợ giảng (TA)  
> **Repository:** [https://github.com/nthanhwork/K4-3A-E403-Phronesis](https://github.com/nthanhwork/K4-3A-E403-Phronesis)

---

## 🎯 Giới thiệu Dự án

### Bối cảnh & Vấn đề Cốt lõi (The Problem)
Trong các kênh Discord của khóa học AI20K (như `#3a-lab-e403` và `#hỏi-đáp`), số lượng tin nhắn trò chuyện, chào hỏi và thảo luận trôi rất nhanh. Dữ liệu thực tế phân tích từ 1.092 tin nhắn thật (`data/discord-pack/k4_messages.csv`) cho thấy:
- Có **136 câu hỏi/kêu cứu kỹ thuật** của học viên.
- **38.2% (52 câu hỏi)** bị tồn đọng quá 2 tiếng chưa có người trả lời.
- Kỷ lục tồn đọng lên tới **12 giờ 25 phút** (tin nhắn `M63574`).
- TA phải cuộn chuột thủ công liên tục 15–20 phút mỗi ca trực nhưng vẫn bỏ sót câu hỏi.

### Giải pháp: Triage Hub `/remaining-questions`
Một lệnh Slash Command native trên Discord trả về **Tin nhắn ẩn riêng tư (Ephemeral Message)** chỉ TA nhìn thấy:
1. **Quét tự động trong 12h:** AI lọc ra các câu hỏi kỹ thuật và chuyên cần chưa có người giải quyết.
2. **Gom cụm chủ đề:** Phân loại vào 4 nhóm nghiệp vụ (*Kỹ thuật & Bài Lab, Logistics & Chuyên cần, Khảo sát & Nhóm, Ngoài phạm vi*).
3. **1-Click Jump Link:** TA bấm vào câu hỏi để màn hình Discord tự động nhảy đến tin nhắn gốc và làm nổi bật để trả lời ngay lập tức.
4. **Vòng lặp đóng (Closed-loop):** Câu hỏi tự động biến mất khỏi hàng đợi khi TA đã gửi phản hồi.

---

## 👥 Danh sách Thành viên & Phân công Nhiệm vụ (Rubric R7)

Chi tiết xem tại [`TEAMMATES.md`](TEAMMATES.md):

| STT | Thành viên | MSSV | Vai trò chính | Phân công cụ thể |
| :---: | :--- | :---: | :--- | :--- |
| 1 | **Nguyễn Thái Anh** | 2A202602810 | Lead Developer & Core Architect | Thiết kế Spec (§1, §4, §6), sơ đồ luồng `docs/flow.md`, phát triển Core AI Engine (`codebase/triage_engine.py`), Server live (`codebase/server.py`), kịch bản demo (`codebase/live_demo.py`) và quản trị Git. |
| 2 | **Ngọ Doãn Ngọc** | 2A202602635 | Team Leader & Product Manager | Điều phối tiến độ tổng thể, đại diện nhóm nộp Form các mốc CP1–CP5, thiết kế Prompt System cho Triage Hub, định nghĩa tiêu chí nghiệm thu và review chất lượng sản phẩm. |
| 3 | **Hoàng Ngọc Đăng Khoa** | 2A202602790 | Data Analyst & Evaluation Specialist | Khai phá dữ liệu chatlog `data/discord-pack/k4_messages.csv`, xây dựng bộ dữ liệu kiểm thử Golden Set 40 cases (§7), thực thi script đánh giá `eval/run_eval.py` và phân tích lỗi `eval/run_results.md`. |
| 4 | **Đoàn Quang Minh** | 2A202602711 | Media Lead & UX Validation | Phụ trách quay video demo 30s thực tế, kiểm thử trải nghiệm giao diện người dùng theo 5 nguyên tắc HAX/PAIR, xây dựng kịch bản trình chiếu slide demo CP5 và phản biện vòng CP6. |

---

## 📁 Cấu trúc Thư mục Repository

```
K4-3A-E403-Phronesis/
├── codebase/                        # Mã nguồn ứng dụng & prototype
│   ├── triage_engine.py             # Module quyết định trung tâm gọi API OpenAI gpt-4o-mini thật
│   ├── live_demo.py                 # Kịch bản chạy live terminal phục vụ quay video 30s
│   ├── server.py                    # Server HTTP cục bộ phục vụ API /api/triage và Web Prototype
│   ├── index.html                   # Giao diện Discord Dark Mode tích hợp tab Live AI
│   └── prototype/index.html         # Bản sao lưu prototype độc lập
├── eval/                            # Bộ dữ liệu & báo cáo kiểm thử (Rubric R4)
│   ├── golden_set.json              # 40 test cases độc lập phủ đủ 4 taxonomy classes
│   ├── run_eval.py                  # Script runner tự động đánh giá trọn bộ 40 test cases
│   ├── run_results.md               # Báo cáo đánh giá sơ bộ lượt 1, bảng % và phân tích sai lệch
│   └── logs/                        # 125+ tệp log JSON ghi nhận toàn bộ prompt và raw response
├── docs/                            # Tài liệu phân tích thiết kế
│   └── flow.md                      # Sơ đồ luồng trạng thái 4 đường trải nghiệm (Mermaid)
├── spec.md                          # Bản đặc tả kỹ thuật hoàn chỉnh 9 phần (Rubric R1-R4)
├── TEAMMATES.md                     # Bảng phân công nhiệm vụ thành viên
└── README.md                        # Hướng dẫn tổng quan dự án
```

---

## ⚡ Hướng dẫn Chạy Thử & Kiểm chứng Kỹ thuật

### 1. Chạy Demo Thời gian thực (Live 30s Terminal Demo)
```bash
python3 codebase/live_demo.py
```
*Chạy 3 ca kiểm thử đại diện (lỗi kỹ thuật thật, thắc mắc điểm danh E403, và chặn tấn công Prompt Injection) với thời gian thực ~15-20 giây, hiển thị trực quan latency và log trace.*

### 2. Chạy Trọn bộ 40 Test Cases (Evaluation Runner)
```bash
python3 eval/run_eval.py
```
*Tự động gọi AI thật qua 40 trường hợp kiểm thử, đo đạc Precision, Recall, F1, Topic, Urgency và tự động sinh báo cáo `eval/run_results.md`.*

### 3. Trải nghiệm Giao diện Web Discord Prototype
```bash
python3 codebase/server.py
# Mở trình duyệt tại: http://localhost:8000
```
*Chuyển sang tab **"⚡ Live AI Test"** để gõ tin nhắn bất kỳ hoặc chọn mẫu test và xem AI phân loại thời gian thực.*

---

## 📊 Kết quả Đo lường Đạt chuẩn (Quality Bar vs Thực tế Run 1)

| Chỉ số đo lường (Metric) | Kết quả Run 1 (40 cases) | Quality Bar cam kết | Trạng thái |
| :--- | :---: | :---: | :---: |
| **Độ chính xác lọc câu hỏi (Triage)** | **100.0%** (40/40) | $\ge 85.0\%$ | ✅ Vượt chỉ tiêu |
| **Precision (Độ chuẩn xác)** | **100.0%** (31/31) | $\ge 85.0\%$ | ✅ Đạt |
| **Recall (Tỷ lệ không bỏ sót)** | **100.0%** (31/31, $FN=0$) | $\ge 90.0\%$ | ✅ Đạt tuyệt đối |
| **F1-Score** | **100.0%** | $\ge 85.0\%$ | ✅ Đạt |
| **Độ chính xác gom cụm chủ đề (Topic)** | **92.5%** (37/40) | $\ge 80.0\%$ | ✅ Đạt |
| **Độ chính xác mức khẩn cấp (Urgency)** | **60.0%** (24/40) | $\ge 60.0\%$ | ✅ Đạt |
| **Full Match (Khớp trọn vẹn cả 3 tiêu chí)**| **57.5%** (23/40) | $\ge 50.0\%$ | ✅ Đạt |
| **Độ trễ trung bình (Latency)** | **1.60s** / request | $\le 3.0\text{s}$ | ✅ Đạt |
