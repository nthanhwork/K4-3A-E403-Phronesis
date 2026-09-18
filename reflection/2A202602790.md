# Bản Thu Hoạch Cá Nhân (Reflection) — Hoàng Ngọc Đăng Khoa
> **Họ và tên:** Hoàng Ngọc Đăng Khoa  
> **Mã học viên:** 2A202602790  
> **Lớp:** K4-3A · **Phòng:** E403 · **Nhóm:** Phronesis  
> **Dự án:** Track B2 — Triage Hub `/remaining-questions`

---

## 1. Vai trò chính trong nhóm
- **Data Analyst & Evaluation Specialist (Chuyên viên Phân tích Dữ liệu & Đánh giá AI)**.
- Chịu trách nhiệm khai phá dữ liệu chatlog thực tế, xây dựng bộ dữ liệu kiểm thử Golden Set 40 cases, thực thi script đánh giá benchmark và phân tích nguyên nhân sai lệch kỹ thuật.

---

## 2. Phần việc cụ thể đã trực tiếp thực hiện
1. **Khai phá Dữ liệu Lớn (Data Mining — Chuẩn B trong Spec §1):**
   - Trực tiếp xử lý file chatlog thực tế `data/discord-pack/k4_messages.csv` gồm **1.092 tin nhắn**.
   - Viết script Python lọc và thống kê: phát hiện **136 câu hỏi** (12.5% volume), **52 câu tồn đọng > 2 giờ** (38.2%), tìm ra kỷ lục tồn đọng thực tế **12 giờ 25 phút** (tin nhắn `M63574` của học viên D3082).
   - Trích xuất 7 trích dẫn nguyên văn kèm mã tin nhắn phục vụ làm bằng chứng kiểm chứng được cho Slide 1 và Spec §1.
2. **Xây dựng Bộ Dữ Liệu Kiểm Thử Golden Set 40 Cases (`eval/golden_set.json`):**
   - Mở rộng quy mô từ 20 lên **40 test cases độc lập**, trong đó **34/40 ca (85%)** lấy từ dữ liệu thật.
   - Thiết kế nhãn kiểm thử chuẩn xác phủ kín 4 lớp taxonomy: 5 ca Lớp ① Nguồn sự thật, 4 ca Lớp ② Mơ hồ, 3 ca Lớp ③ Ngoài phạm vi, 8 ca Lớp ④ Đặc thù nghiệp vụ, 18 ca Phổ biến và 2 ca Edge cases.
3. **Thực thi Đánh giá Tự Động & Lập Báo Cáo (`eval/run_eval.py` & `eval/run_results.md`):**
   - Chạy kiểm thử tự động toàn bộ 40 ca qua model OpenAI `gpt-4o-mini`.
   - Sinh **125 tệp log JSON** trong thư mục `eval/logs/` ghi vết: prompt đầu vào, raw response, tokens và latency từng request.
   - Thống kê ma trận nhầm lẫn và viết báo cáo mổ xẻ nguyên nhân kỹ thuật chi tiết cho 17 ca chưa đạt Full Match ở Run 1.

---

## 3. AI đã hỗ trợ tôi như thế nào trong quá trình làm việc?
- **Tự động hóa Script Phân Tích Dữ Liệu:** AI hỗ trợ viết script trích xuất regex tiếng Việt, xử lý múi giờ UTC sang giờ Việt Nam (`created_at_vn`) để tính toán chính xác thời gian phản hồi giữa học viên và trợ giảng trong tệp CSV.
- **Tạo khung Test Harness:** Sử dụng AI để sinh cấu trúc script kiểm thử `eval/run_eval.py`, tính toán tự động các chỉ số Precision, Recall, F1-Score và Full Match Rate theo đúng công thức định lượng trong `spec.md` §7.
- **Phát hiện Mẫu Lỗi (Error Pattern Recognition):** Cùng AI gom nhóm 16 ca lỗi Urgency thành 2 cụm nguyên nhân chính: cụm ngôn từ lịch sự và cụm câu hỏi giao thoa mốc thời gian.

---

## 4. Một bài học sâu sắc nhất từ failure case của chính nhóm
- **Hiện tượng Giao Thoa Đa Chủ Đề (Multi-label Overlap):**
  - Trong Run 1, có 3 test cases (TC03, TC04, TC33) bị mô hình phân loại nhầm giữa `Logistics & Chuyên cần` và `Khảo sát & Nhóm`.
  - **Nguyên nhân:** Câu hỏi của học viên chứa cả hai yếu tố: vừa hỏi về deadline nộp danh sách (thủ tục) vừa hỏi về quy định ghép 3 bạn vào đội (nhóm). Do mô hình hiện tại áp dụng Single-label classification nên buộc phải chọn 1 nhãn duy nhất, dẫn đến lệch với nhãn kỳ vọng của con người.
  - **Bài học:** Các bài toán phân loại văn bản hội thoại thực tế rất hiếm khi phân định rạch ròi 1 nhãn duy nhất. Cần xây dựng cơ chế Multi-label tagging hoặc phân cấp phân loại theo mức độ ưu tiên nghiệp vụ.

---

## 5. Tự kiểm tra quy tắc "Vibe-coding" (Sẵn sàng giải thích trước Giám khảo CP6)
- **Phương pháp đếm kiểm chứng lại được (Reproducible Counting Method):** Sử dụng Pandas đọc `k4_messages.csv`, lọc các dòng có `is_bot == False`, dùng biểu thức chính quy nhận diện dấu hỏi `?` hoặc các từ khóa đặc trưng ("cho em hỏi", "lỗi", "giúp em"), sau đó tính khoảng cách thời gian $\Delta t = t_{\text{reply}} - t_{\text{msg}}$ để xác định các câu hỏi tồn đọng $> 2$ giờ.
- **Ý nghĩa của 125 logs trong `eval/logs/`:** Mỗi lượt chạy kiểm thử sinh ra 1 file JSON độc lập lưu đầy đủ `prompt_input`, `raw_response` của OpenAI và latency thực tế. Đây là bằng chứng vật lý để giám khảo đối soát trực tiếp, chứng minh nhóm chạy AI thật 100% chứ không giả lập kết quả.
