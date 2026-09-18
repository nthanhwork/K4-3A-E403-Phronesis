# Reflection — Hoàng Ngọc Đăng Khoa

**Mã học viên:** 2A202602790 · **Vai trò:** Data Analyst & Evaluation Specialist

> Bốn phần theo rubric reflection của khoá *(`04-rubric.md` — mục *Reflection cá nhân*)*.

---

## 1. Vai trò & phần cá nhân làm

- **Khai phá dữ liệu (EDA):** Trực tiếp rà soát, trích xuất và phân tích toàn bộ tập dữ liệu chatlog thực tế `data/discord-pack/k4_messages.csv` (1.092 tin nhắn thực tế của khoá K4) để xác định các mẫu câu hỏi thường gặp, tỷ lệ tin nhắn rác và hành vi đặt câu hỏi của học viên.
- **Xây dựng Golden Set 40 cases (`eval/golden_set.json`):** Thiết kế bộ testbench kiểm thử chuẩn bao phủ toàn diện 4 lớp chỗ khó thực tế:
  1. *Lớp 1: Nguồn sự thật (Single Source of Truth)* — Hỏi về quy chế, điểm danh bù, kích hoạt thẻ học viên, chính sách lab.
  2. *Lớp 2: Mơ hồ / Thiếu thông tin* — Tin nhắn gửi rời rạc, chụp màn hình thiếu context, gọi TA chung chung ("anh ơi tới zone 2").
  3. *Lớp 3: Ngoài phạm vi / Vượt thẩm quyền* — Nhờ làm hộ bài lab, hỏi môn học trường ngoài, hỏi việc cấp giấy hoãn NVQS.
  4. *Lớp 4: Đặc thù nghiệp vụ & Edge Cases* — Tin nhắn cảm ơn, thảo luận phiếm, cùng ca cố tình tấn công Prompt Injection ghi đè System Prompt.
- **Vận hành & đo lường kiểm thử (`eval/run_eval.py`):** Phối hợp cùng thành viên Nguyễn Thái Anh chạy kiểm thử tự động trên API thật, thu thập kết quả và tính toán các chỉ số: Triage Accuracy (100.0%), Topic Clustering Accuracy (92.5%), Urgency Accuracy (60.0%), Full Match (57.5%), Latency trung bình 1.60s.
- **Mổ xẻ nguyên nhân sai lệch kỹ thuật (`eval/run_results.md`):** Viết báo cáo phân tích chi tiết từng ca sai lệch (17/40 ca lệch phụ), bảo đảm cam kết đánh giá AI trung thực, không "nấu số liệu".
- **Điểm khó nhất & Quyết định quan trọng:** Khó nhất là định nghĩa nhãn kỳ vọng (Ground Truth) cho mức độ khẩn cấp (`Urgency`) vì ranh giới rất mong manh giữa cảm xúc chủ quan và tính cấp thiết nghiệp vụ. Tôi đã đưa ra quyết định nhóm kiên định giữ nguyên dữ liệu gốc và chỉ số Full Match 57.5% để nhìn thẳng vào sự thật kỹ thuật, kiên quyết không sửa nhãn test case hay hạ quality bar chỉ để lấy số đo đẹp nộp bài. Chỗ tôi làm chưa tốt là ở Run 1 chưa thiết kế thêm few-shot examples trong prompt nên khiến mô hình bị nhầm lẫn ở mức độ khẩn cấp.

---

## 2. AI hỗ trợ tôi thế nào

- **Công cụ sử dụng:** Antigravity CLI và Claude/ChatGPT hỗ trợ viết script Python xử lý dữ liệu, trích lọc regex các trường dữ liệu JSON và format bảng Markdown thống kê.
- **Chỗ AI làm nhanh vượt trội:** AI giúp sinh nhanh khung script phân tích ma trận nhầm lẫn (Confusion Matrix) và tự động bóc tách 40 kết quả test log thành bảng so sánh song song trong vài giây, tiết kiệm hàng giờ gõ tay thủ công.
- **Chỗ AI sai và tôi phải sửa tay (Bắt lỗi AI):** 
  - Khi nhờ AI gợi ý nhãn Ground Truth ban đầu cho 40 test cases, AI bị ảo giác và đánh giá ngữ cảnh hoàn toàn sai lệch ở ca **SYN_04** (học viên hỏi nhờ sửa đồ án môn Vi xử lý bên Bách Khoa). AI tự động gán nhãn `urgent` chỉ vì thấy có từ "đồ án tốt nghiệp", trong khi thực tế đây là câu hỏi hoàn toàn ngoài phạm vi chương trình VinAI (phải gán nhãn `low` hoặc reject).
  - Tương tự ở ca **TC07** (hỏi về deadline ghép đội kết thúc sớm), AI ban đầu gom vào chủ đề `Khảo sát & Nhóm`, nhưng dưới góc nhìn nghiệp vụ điều phối đây là vấn đề thời hạn/lịch trình thuộc `Logistics & Chuyên cần`. Tôi phải loại bỏ các phán đoán tự động của AI và trực tiếp rà soát bằng tay 100% nhãn Ground Truth để đảm bảo chuẩn tham chiếu tuyệt đối khách quan.

---

## 3. Một bài học từ case fail của chính nhóm

- **Sự cố xảy ra:** Trong đợt chạy kiểm thử Run 1 (CP3), dù hệ thống đạt độ chính xác lọc câu hỏi tuyệt đối **100% (40/40)**, chỉ số khớp hoàn hảo cả 3 tiêu chí (**Full Match**) chỉ đạt **57.5%**, trong đó độ chính xác nhận diện mức khẩn cấp (**Urgency**) bị tụt xuống **60.0%**, suýt chạm ngưỡng sàn chấp nhận được.
- **Nguyên nhân gốc rễ (Root Cause):** Khi tôi rà soát chi tiết 17 ca lệch điểm trong `eval/run_results.md`, tôi phát hiện có tới 16/17 ca bị lệch duy nhất ở trường `urgency_level` (mô hình đoán `medium`/`low` trong khi nhãn kỳ vọng là `urgent`). LLM bị "đánh lừa" bởi sự lịch sự của học viên: khi học viên mở đầu bằng *"Dạ em chào anh chị..."*, *"Nhờ các anh chị hỗ trợ giúp em chút..."* (như ca điểm danh bù TC14, lỗi kích hoạt thẻ học viên TC23, hay fork code bài lab TC26), mô hình AI mặc định xem câu nói nhẹ nhàng này có mức độ ưu tiên thấp (`medium`), mà không nhận ra rằng đây là các vấn đề mang tính "chặn tiến độ" (blocker) sát giờ học cần TA xử lý ngay.
- **Tôi hiểu sai ở đâu & Bài học:** Ban đầu tôi ngây thơ cho rằng chỉ cần mô tả tiêu chuẩn khẩn cấp bằng định nghĩa chữ trong System Prompt (zero-shot) là LLM tự hiểu được ngữ cảnh. Nhưng thực tế mô hình ngôn ngữ rất nhạy cảm với văn phong (tone of voice) bề mặt. Bài học rút ra là: **Không thể đo lường AI bằng cảm tính; và đối với các nhiệm vụ đánh giá ngữ nghĩa phức tạp, zero-shot prompt không bao giờ đủ**.
- **Cách nhóm giải quyết & Lần sau làm khác:** Thay vì sửa lại ground truth để điểm tăng lên 80%, nhóm tôi quyết định công khai toàn bộ 17 ca lệch này trong báo cáo, đồng thời tôi thiết kế ngay 3 ví dụ thực tế (few-shot in-context learning) mô phỏng chính xác các trường hợp "học viên hỏi lịch sự nhưng việc cực kỳ gấp" để đưa vào prompt cho Run 2 (CP4/CP5), giúp mô hình hiệu chuẩn lại thang đo khẩn cấp một cách bền vững.

---

## 4. Nếu làm lại

- Nếu được làm lại từ đầu dự án, tôi sẽ xây dựng bộ dữ liệu kiểm thử Golden Set song song với việc gắn nhãn chéo (cross-annotation) giữa ít nhất 2 thành viên trong nhóm để loại bỏ hoàn toàn tính chủ quan ngay từ phút đầu tiên.
- Đồng thời, tôi sẽ triển khai kỹ thuật Few-Shot Calibration ngay từ phiên bản prompt đầu tiên thay vì dùng Zero-Shot, và chuẩn hóa pipeline tự động sinh log variance dạng biểu đồ trực quan để nhóm kịp thời tinh chỉnh prompt trước mỗi mốc nộp bài.

---

