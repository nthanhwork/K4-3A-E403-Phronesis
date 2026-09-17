### 📌 PHẦN 1: Checkpoint 3 gồm những công việc cụ thể nào?

Mục tiêu cốt lõi của CP3 là "Đưa AI thật vào sản phẩm và đo lường số liệu thực tế" (không được dùng data hardcode nữa). Bạn cần hoàn thành 4 sản phẩm đầu ra
(Deliverables):

1. Module gọi AI thật (codebase/):
   • Viết mã nguồn gọi API LLM thật (Gemini, OpenRouter hoặc OpenAI) tại mắt xích quyết định trung tâm:
   • Nhận đầu vào là tin nhắn Discord.
   • AI quyết định: (1) Đây có phải câu hỏi chưa được giải quyết không? (2) Thuộc nhóm chủ đề nào?
   • Bắt buộc có cơ chế ghi log (logging) lưu lại prompt đầu vào và raw response của mô hình để ban giám khảo đối chiếu kỹ thuật.
2. Bộ dữ liệu kiểm thử Golden Set (eval/golden_set.json):
   • Tối thiểu 20 trường hợp kiểm thử (test cases) độc lập.
   • Phủ đủ 4 lớp chỗ khó (mỗi lớp ≥ 2 case):
   • ① Nguồn sự thật (hallucination/đoán mò)
   • ② Mơ hồ/thiếu thông tin (câu hỏi cộc lốc)
   • ③ Ngoài phạm vi/thẩm quyền (hỏi giải bài hộ)
   • ④ Đặc thù nghiệp vụ (thread con, spam nhiều tin liên tiếp).
   • Trong đó ≥ 10 trường hợp phải trích xuất từ tin nhắn thật (từ data/discord-pack/ hoặc kênh Discord của lớp).
3. Bảng đo lường kết quả lượt 1 (eval/run_results.md):
   • Chạy toàn bộ 20 case qua module AI thật.
   • Thống kê: Số ca đạt, số ca sai, tỷ lệ % đạt.
   • Phân tích nguyên nhân sai lệch: (Quy tắc của BTC: 12/20 ca pass mà phân tích sâu sắc nguyên nhân vì sao AI phân loại sai thì ăn trọn điểm; bịa số 20/20
   không có log sẽ bị trừ toàn bộ điểm).
4. Video quay màn hình 30 giây:
   • Thao tác trực tiếp: Nhập câu hỏi/bấm lệnh ➔ Thấy AI xử lý và trả về kết quả thật theo thời gian thực (không cần dựng hình hay lồng tiếng).

──────

### 👤 PHẦN 2: Phần nào AI hỗ trợ được và Phần nào BẮT BUỘC con người can thiệp?

| Hạng mục                           | Antigravity AI hỗ trợ làm ngay                                  | BẮT BUỘC con người phải can thiệp                              |
| ---------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------- |
| 1. Code AI thật                    | Viết script Python gọi API Gemini/OpenRouter, xử lý prompt,     | Bạn cần đảm bảo file .env trên máy có sẵn API Key (Gemini hoặc |
| phân loại câu hỏi và ghi file log. | OpenRouter) còn hoạt động.                                      |
| 2. Golden Set (20 case)            | Trích xuất tin nhắn thật từ data/discord-pack/, format thành    | Cả nhóm đọc lướt qua 20 case để xác nhận các tình huống đúng   |
| file JSON chuẩn 4 lớp chỗ khó.     | thực tế của lớp học.                                            |
| 3. Đo lường & Viết báo cáo         | Viết script tự động chạy 20 case, chấm điểm Precision/Recall và | Đọc bảng kết quả để hiểu rõ con số (để lúc pitch nói được).    |
| xuất bảng Markdown.                |
| 4. Video demo 30s                  | Cung cấp giao diện / luồng thao tác mẫu để quay.                | Bắt buộc con người quay màn hình: Dùng OBS / trình quay màn    |
|                                    | hình quay 30 giây và up lên Google Drive.                       |
| 5. Nộp form CP3                    | Không thể nộp thay.                                             | Bắt buộc nhóm trưởng (Ngọc): Điền form nộp bài của BTC trước   |
|                                    | 16:00.                                                          |

──────

### 👥 PHẦN 3: Phân công nhiệm vụ cho từng thành viên trong nhóm

Vì bạn (Thái Anh) đang giữ máy tính và repo chính, còn bạn Ngọc là Nhóm trưởng, nhóm nên phối hợp nhịp nhàng như sau:

#### 1. Bạn (Nguyễn Thái Anh — Kỹ thuật & Vận hành máy):

• Cùng Antigravity dựng script gọi API thật (codebase/triage_engine.py) và chạy file đánh giá (eval/run_eval.py).
• Bật giao diện demo để cùng quay video 30 giây thao tác thực tế.
• Thực hiện lệnh git add codebase/ eval/, commit và push lên GitHub.

#### 2. Bạn Ngọ Doãn Ngọc (Nhóm trưởng — Điều phối & Nộp bài):

• Mở form nộp CP3 của BTC từ sớm để xem form yêu cầu những trường thông tin gì (link repo, số đo %, link video...).
• Kiểm tra bộ 20 case trong eval/golden_set.json xem đã đủ 4 lớp chỗ khó chưa.
• Lấy số đo từ file eval/run_results.md và link video để đại diện nhóm nộp form trước 16:00.

#### 3. Bạn Hoàng Ngọc Đăng Khoa (Data & Phân tích lỗi):

• Đọc kết quả chạy test lượt 1 (những ca AI phân loại sai) và viết 3–4 câu phân tích nguyên nhân vào eval/run_results.md (ví dụ: "AI nhận nhầm tin nhắn chào hỏi
thành câu hỏi vì có chứa dấu chấm hỏi...").
• Chuẩn bị sẵn tài liệu cho CP4 tối nay.

#### 4. Bạn Đoàn Quang Minh (Media & Kiểm thử Video):

• Phụ trách việc quay màn hình thao tác 30 giây (đảm bảo video rõ nét, đúng trong khoảng 25–35 giây, thấy rõ thao tác lệnh và kết quả AI trả về).
• Tải video lên Google Drive, bật quyền "Bất kỳ ai có liên kết đều xem được" và gửi link cho Ngọc nộp.
──────

### ⏱️ Lộ trình thời gian từ giờ đến 16:00:

• 11:00 – 12:00: Dựng bộ eval/golden_set.json (20 case) và script AI thật codebase/triage_engine.py.
• 12:00 – 13:30: Nghỉ trưa.
• 13:30 – 14:30: Chạy đánh giá lượt 1, sinh file log và viết eval/run_results.md.
• 14:30 – 15:15: Quay video màn hình 30 giây, upload Google Drive.
• 15:15 – 15:45: Git commit & push repo; Ngọc điền form nộp bài.
• 16:00: Hạn chốt — Hoàn thành an toàn!

Bạn có muốn chúng ta bắt tay vào Bước 1: Tạo bộ dữ liệu kiểm thử 20 case (eval/golden_set.json) và viết module gọi AI thật ngay bây giờ không?
