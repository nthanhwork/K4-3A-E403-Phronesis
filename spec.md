# AI SPEC — Triage Hub /remaining-questions: Hàng Đợi Giải Cứu Câu Hỏi Tồn Đọng Cho TA
> **Nhóm:** Phronesis · Phòng E403 · Lớp 3A · Batch 04  
> **Track:** B · Trợ lý Học viên (Discord) — **Đề:** B2 · Tính năng mới cho TA  
> **Loại:** [ ] Tối ưu tính năng có sẵn  [x] Tính năng mới  

---

## §1. User & Job

- **Job executor + workflow:**
  - *Người thực hiện:* Trợ giảng (TA) / Lab Coach trực hỗ trợ kỹ thuật trên Discord của khóa AI20k.
  - *Quy trình hiện tại:* TA vào ca trực ➔ Cuộn chuột lội kênh thủ công qua hàng trăm tin nhắn ở `# 3a-lab-e403` và `# hỏi-đáp` ➔ Cố gắng tìm xem học viên nào đang hỏi bài ➔ Trả lời từng người ➔ Dễ bỏ sót các câu hỏi bị trôi hoặc nhầm lẫn câu nào đã có người giải quyết.
- **Core JTBD (Không tên sản phẩm/AI trong câu):**
  > *"Giúp người trực hỗ trợ kỹ thuật phát hiện và xử lý kịp thời toàn bộ câu hỏi của người học đang bị bỏ sót trong ca trực mà không phải rà soát thủ công từng dòng tin nhắn."*
- **Problem statement (KHÔNG chữ AI):**
  > Kênh thảo luận Discord có quá nhiều tin nhắn trò chuyện lẫn hỏi bài khiến tin nhắn trôi rất nhanh; người trực hỗ trợ phải cuộn chuột thủ công liên tục nhưng vẫn bỏ sót câu hỏi kỹ thuật của người học từ 7 đến 24 tiếng mà không hay biết, khiến người học bế tắc và nản lòng.
- **Evidence (Chuẩn A và Chuẩn B — Log đầy đủ trong repo):**
  - *Số liệu khảo sát ($n = 10$ TA/Lab Coach thực tế ngày 16–17/9/2026):*
    - **90% (9/10 TA)** xác nhận mất thời gian mỗi ngày chỉ để cuộn chuột lội kênh tìm câu hỏi (thời gian cuộn từ 10 đến 60 phút/ngày, trung bình ~22 phút/ngày).
    - **Kỷ lục câu hỏi bị tồn đọng:** Lên tới **24 tiếng** (TA mốc 20:29), **12 tiếng** (TA mốc 19:13), **6–10 tiếng** (TA mốc 19:14), **7 tiếng** (TA mốc 19:17 do bị ốm), và **4 tiếng** (TA mốc 10:15).
    - **Tỷ lệ trùng lặp:** **13% – 50%** (hoặc 20–30 câu hỏi lặp lại/ngày), khiến TA nản lòng dẫn đến xử lý bằng cách *"bỏ qua luôn"* hoặc phải trả lời đi trả lời lại.
    - **60% (6/10 TA)** sẵn sàng tham gia dùng thử giải pháp mới ngay lập tức.
  - *≥5 Quote nguyên văn từ người dùng thật:*
    1. *"Quá nhiều tin mà phải đọc hết"* — TA (Timestamp 19:16:20)
    2. *"Bị trôi tin nhắn"* — TA (Timestamp 19:18:21)
    3. *"Khó nắm bắt tình hình nếu bỏ lỡ câu chuyện khá lâu"* — TA (Timestamp 19:17:23)
    4. *"Bỏ qua luôn"* & *"Bỏ qua"* (khi gặp câu hỏi trùng lặp) — TA (Timestamp 19:17:23, 10:14:19)
    5. *"Mất thời gian đi research"* & *"Dò thủ công"* — TA (Timestamp 19:14:28)
    6. *"Tìm bằng ctrl F nhưng phải cuộn đến gần vùng đó"* — TA (Timestamp 19:47:00)
    7. *"Phải lướt thủ công để tìm, lướt bằng tay"* & *"đợi load khá lâu và nhìn khá rối mắt"* — TA (Timestamp 10:15:35, 10:14:19)

---

## §2. Impact & quyết định chọn

- **Bảng impact ≥3 ứng viên:**
  | Ứng viên tính năng | Bao nhiêu người | Tần suất | Tốn gì mỗi lần | Khả thi | Đánh giá |
  |---|---|---|---|---|---|
  | **1. Hàng đợi câu hỏi tồn đọng (`/remaining-questions`)** | 10–15 TA / Lab Coach | 5–8 lần/ca trực | 15–60 phút lội kênh/ngày, áp lực sót tin 12–24h | Rất cao (heuristic + LLM filter/cluster) | **CHỌN** |
  | **2. Bot tự động trả lời code/lab thay TA** | 1.000 học viên | Hàng ngày | Nguy cơ trả lời sai gây trượt lab, hallucination cao | Thấp (Cost of error cực kỳ nghiêm trọng) | **LOẠI** |
  | **3. Bản tin tổng hợp cuối ngày đăng lên kênh chung** | 10 TA | 1 lần/ngày | Đã có bot cũ nhưng TA không đọc vì không bấm vào xử lý được | Trung bình (Không có tính hành động) | **LOẠI** |

- **Ứng viên ĐÃ LOẠI + vì sao:**
  - *Ứng viên 2 (Auto-reply):* Chi phí sai sót quá lớn (Cost of error cao), học viên có thể nhận hướng dẫn sai làm hỏng môi trường máy; vi phạm nguyên tắc an toàn sư phạm.
  - *Ứng viên 3 (Bản tin cuối ngày):* Chỉ mang tính thông báo một chiều, thiếu tính hành động tức thì, gây rác kênh chung và không giúp TA giải quyết được các ca đang bị kẹt lúc trực.
- **Ứng viên CHỌN + vì sao (bằng số):**
  - Chọn **Ứng viên 1 (`/remaining-questions`)** vì giải quyết trực tiếp kỷ lục tồn đọng **12–24 tiếng** kéo xuống dưới **30 phút**; tiết kiệm trung bình **15–60 phút/ngày** cuộn chuột cho mỗi TA; và có **6/10 TA (60%)** sẵn sàng làm Willing Users dùng thử ngay.

---

## §3. Giải pháp tương tự đã nghiên cứu

- **Bot "Trợ lý Kute" (Bot hiện tại của khóa AI20k):**
  - *Flow:* Tự động tổng hợp bản tin đăng lên kênh chung vào cuối ngày.
  - *Đáng học:* Tự động quét và gom tin nhắn theo ngày.
  - *Đáng né:* Chèn lỗi ký tự ("nguồn tham chiếu"), tóm tắt cắt cụt, đăng công khai gây loãng kênh, không có link bấm thẳng vào tin nhắn học viên cần trả lời.
  - *Mình khác gì:* Trả về dạng tin nhắn ẩn (Ephemeral) riêng cho TA; lọc câu hỏi chưa trả lời trong 12h; có **1-Click Jump Link** cuộn thẳng đến tin nhắn gốc; có vòng lặp đóng (tự động xóa câu hỏi khi TA đã phản hồi).
- **Zendesk / Freshdesk Ticket Queue:**
  - *Flow:* Nhận yêu cầu và xếp vào hàng đợi hỗ trợ dạng vé (Ticket FIFO).
  - *Đáng học:* Cơ chế hàng đợi câu hỏi chưa giải quyết và phân loại theo mức độ ưu tiên/chủ đề.
  - *Đáng né:* Bắt buộc mở tab trình duyệt riêng, quy trình tạo ticket phức tạp, không phù hợp với văn hóa chat real-time của Discord.
  - *Mình khác gì:* Tích hợp 100% native trong Discord thông qua Slash Command, TA không cần rời khỏi không gian làm việc.

---

## §4. Thiết kế

- **Lát cắt MỘT CÂU (1 user · 1 việc · 1 quyết định AI · 1 kết quả):**
  > *"Một TA gõ lệnh `/remaining-questions` trên Discord ➔ AI quét tin nhắn 12 giờ qua, lọc câu hỏi kỹ thuật chưa được phản hồi và phân loại theo chủ đề / thời gian dưới dạng tin nhắn ẩn riêng tư (Ephemeral Message, tối đa 15 câu) ➔ TA bấm chọn câu hỏi để nhảy thẳng ngay đến tin nhắn gốc của học viên trên Discord để xem toàn bộ ngữ cảnh và giải đáp ➔ Hệ thống tự động đánh dấu đã giải quyết sau khi TA phản hồi."*

- **Non-goals (≥3 thứ KHÔNG build):**
  1. *KHÔNG tự động tạo câu trả lời thay TA gửi cho học viên:* Con người (TA) luôn là người trực tiếp đọc ngữ cảnh và gửi câu trả lời.
  2. *KHÔNG xây dựng dashboard web bên ngoài:* Toàn bộ trải nghiệm gói gọn trong giao diện Discord qua Slash Command để giảm thiểu chuyển đổi ngữ cảnh.
  3. *KHÔNG tóm tắt nội dung câu hỏi qua AI:* Tránh tuyệt đối rủi ro bóp méo ngữ cảnh khi gặp câu hỏi mơ hồ, chỉ hiển thị trích đoạn nguyên văn và link nhảy trực tiếp.

- **Mức prototype nhắm tới:** `[ ] Sketch  [x] Mock (CP2)  [x] Working (CP3)`
  - *Phần Mock (CP2):* Dữ liệu tin nhắn giả lập từ ảnh chụp màn hình thật phòng E403 (`codebase/prototype/index.html`), cơ chế chuyển tab, giới hạn 15 câu và mô phỏng 1-Click Jump.
  - *Phần Thật (CP3):* Gọi API LLM thật (Gemini / OpenRouter) để phân loại câu hỏi chưa trả lời và trích xuất embedding gom cụm chủ đề; kiểm thử trên Golden set ≥20 case.

- **Automation:** `[x] augment  [ ] conditional  [ ] automate`
  - *Lý do theo Cost-of-error:* Chi phí sai sót trong việc hỗ trợ kỹ thuật và điểm danh là **rất cao** (học viên có thể trượt bài, cấu hình sai hệ thống hoặc bức xúc vì thông tin sai). Vì vậy, hệ thống **bắt buộc dừng ở mức Hỗ trợ (Augment)**: AI chỉ làm nhiệm vụ phát hiện, phân loại và dẫn đường (Triage & Navigation), quyền quyết định nội dung trả lời và xác nhận giải quyết thuộc về TA.

- **§4b. Nguyên tắc đã áp dụng (≥4 — HAX/PAIR):**
  | Nguyên tắc | Áp cụ thể vào đâu trong prototype (`codebase/prototype/index.html`) |
  |---|---|
  | **HAX G1: Make clear what the system can do** (Nêu rõ năng lực hệ thống) | Tiêu đề popup nêu rõ phạm vi: *"📋 Hàng Đợi Câu Hỏi Tồn Đọng (12 Giờ Qua)"* kèm số lượng câu hỏi tìm thấy và thanh trạng thái giới hạn. |
  | **HAX G2: Make clear how well the system can do** (Rõ mức độ tin cậy/ưu tiên) | Gắn nhãn badge thời gian chờ rõ ràng (⏳ Tồn 8h15p, ⏳ Tồn 45p) và trích đoạn nguyên văn để TA tự đánh giá mức độ khẩn cấp. |
  | **HAX G9: Support efficient correction / Dismiss** (Hỗ trợ sửa sai & làm mới nhanh) | Nút `[🔄 Làm mới]` cho phép TA kích hoạt quét lại tức thì; tin nhắn là Ephemeral Message có nút đóng; câu hỏi tự động biến mất khi đã được trả lời. |
  | **HAX G11: Make clear why the system did what it did** (Rõ căn cứ quyết định) | Phân cụm chủ đề hiển thị rõ số lượng câu hỏi thực tế; loại bỏ hoàn toàn việc tóm tắt AI để tránh ảo giác làm TA hiểu sai vấn đề của học viên. |
  | **PAIR: Control & Graceful Degradation** (Quyền kiểm soát của người dùng) | Thao tác 1-Click Jump chuyển TA về tin nhắn gốc trên Discord, giữ nguyên toàn bộ quyền kiểm soát ngữ cảnh và quyết định trả lời cho con người. |

---

## §5. Kiểu lỗi — 4 lớp chỗ khó + kịch bản (≥8)

| Lớp lỗi | Tình huống / Kịch bản cụ thể | Hệ thống xử lý thế nào để tránh fail |
|---|---|---|
| **Lớp 1: Input bẩn / Khó đoán** | Học viên hỏi cộc lốc: *"anh ơi"* hoặc *"lỗi rồi"* | AI nhận diện là câu hỏi nhưng không cố bịa nội dung; giữ nguyên trích đoạn và ưu tiên đưa lên đầu nếu chờ lâu. |
| **Lớp 1: Input bẩn / Khó đoán** | Học viên gửi kèm ảnh chụp màn hình không có chữ | Heuristic nhận diện tin nhắn có đính kèm ảnh và không có text ➔ Gán nhãn "Ảnh chụp màn hình lỗi" để TA bấm vào xem trực tiếp. |
| **Lớp 2: Ngữ cảnh đa tầng** | 1 học viên gửi liên tiếp 4 tin nhắn để giải thích 1 lỗi | AI gom nhóm các tin nhắn liên tiếp của cùng 1 User trong vòng 5 phút thành 1 ca hỗ trợ duy nhất, không tạo 4 mục rác. |
| **Lớp 2: Ngữ cảnh đa tầng** | Câu hỏi đã được bạn khác trả lời trong thread con | AI kiểm tra thread reply; nếu đã có tin nhắn phản hồi sau đó thì tự động loại bỏ khỏi hàng đợi tồn đọng. |
| **Lớp 3: Giới hạn năng lực AI** | 2 câu hỏi dùng từ ngữ khác nhau nhưng cùng lỗi môi trường | Thuật toán gom cụm ngữ nghĩa (Clustering) đưa về cùng 1 nhóm chủ đề để TA xử lý đồng thời. |
| **Lớp 3: Giới hạn năng lực AI** | Prompt injection: Tin nhắn học viên chứa lệnh phá hoại bot | Hệ thống coi toàn bộ tin nhắn học viên là dữ liệu thuần (Untrusted Data), không bao giờ thực thi dưới dạng chỉ dẫn hệ thống. |
| **Lớp 4: Lỗi giao tiếp người-máy** | Hàng đợi có quá nhiều câu hỏi (> 30 câu) gây ngợp | Tích hợp bộ lọc Giới hạn (Limit 15 câu/popup tùy chỉnh) để TA tập trung giải quyết dứt điểm từng đợt, tránh quá tải nhận thức. |
| **Lớp 4: Lỗi giao tiếp người-máy** | TA đã trả lời nhưng danh sách không cập nhật | Nút `[🔄 Làm mới]` cho phép TA ép buộc quét lại realtime để xác nhận câu hỏi đã biến mất. |

---

## §6. Bốn đường đi của trải nghiệm

- **1. Happy path (Đường thuận lợi - AI tự tin cao):**
  TA gõ `/remaining-questions` ➔ Bot trả về Ephemeral Message chỉ mình TA thấy ➔ Danh sách hiển thị 3–6 câu hỏi tồn đọng xếp theo thời gian hoặc chủ đề ➔ TA bấm chọn câu hỏi ➔ Màn hình Discord tự động cuộn đến và nhấp nháy làm nổi bật tin nhắn gốc ➔ TA đọc ngữ cảnh và gõ trả lời học viên ➔ AI tự động loại bỏ câu hỏi khỏi hàng đợi trong lần quét kế tiếp.
- **2. Low-confidence (Đường xử lý khi AI thiếu tự tin / Câu hỏi nhập nhằng):**
  Khi học viên hỏi câu rất ngắn hoặc mơ hồ (*"anh ơi tới zone 2 giúp em"*): AI **tuyệt đối không cố tóm tắt hay suy diễn**. Hệ thống hiển thị nguyên văn câu hỏi kèm nhãn thời gian chờ để TA bấm link nhảy đến trực tiếp hỏi lại học viên.
- **3. Failure / Không căn cứ (Đường xử lý khi không có câu hỏi tồn):**
  Khi quét 12 giờ qua và không phát hiện câu hỏi nào chưa trả lời: Bot phản hồi thông điệp tích cực: *"🎉 Tuyệt vời! Hiện tại không có câu hỏi nào bị tồn đọng quá 30 phút trong 12 giờ qua. Toàn bộ học viên đã được hỗ trợ kịp thời!"*.
- **4. Correction (Cơ chế người dùng can thiệp sửa đổi):**
  Nếu TA thấy một câu hỏi bị phân loại nhầm hoặc vừa mới được giải quyết xong nhưng bot chưa kịp cập nhật ➔ TA bấm nút `[🔄 Làm mới]` để kích hoạt quét lại tức thì; hoặc TA bấm trực tiếp vào tin nhắn để gửi phản hồi, hệ thống sẽ tự động gạch tên khỏi danh sách.
- **Khi bị đòi ngoài phạm vi:**
  Nếu người dùng gõ lệnh hoặc gửi câu hỏi ngoài phạm vi hỗ trợ hàng đợi (ví dụ yêu cầu bot giải bài tập hộ hoặc hỏi thông tin thời tiết) ➔ Bot từ chối lịch sự: *"Lệnh /remaining-questions chỉ dành riêng cho việc rà soát hàng đợi câu hỏi tồn đọng của TA. Để hỏi bài học, bạn vui lòng tag bot Trợ lý học tập."*
- **Case đặc thù domain:**
  - Học viên spam nhiều tin nhắn liên tiếp: AI tự động nhóm các tin nhắn trong vòng 5 phút thành 1 đơn vị câu hỏi.
  - Câu hỏi nhạy cảm hoặc mang tính phàn nàn cá nhân: Chỉ hiển thị trong Ephemeral Message riêng của TA, không công khai danh tính trên kênh chung.

---

## §7. Kiểm thử

- **Chiều chất lượng + Định nghĩa kiểm chứng được:**
  - *Precision (Độ chính xác):* Tỷ lệ các tin nhắn được bot đánh dấu là "câu hỏi tồn đọng" thực sự là câu hỏi kỹ thuật chưa được trả lời (Mục tiêu: $\ge 85\%$).
  - *Recall (Độ bao phủ):* Tỷ lệ các câu hỏi thực tế bị bỏ quên trong kênh được bot phát hiện (Mục tiêu: $\ge 90\%$, đặc biệt các câu chờ $> 4$ tiếng phải đạt $100\%$).
  - *Clustering Accuracy:* Tỷ lệ gom đúng cụm chủ đề cho các câu hỏi trùng lặp (Mục tiêu: $\ge 80\%$).
- **Golden set (≥20 case trích xuất từ `data/discord-pack/`):**
  - Lưu trữ tại: `eval/golden_set.json` (Gồm: 8 câu hỏi kỹ thuật đơn lẻ, 4 câu hỏi trùng lặp cùng lỗi, 3 câu hỏi mơ hồ/cộc lốc, 3 tin chat thường/xã giao, 2 câu hỏi đã có thread reply).
- **Quality bar (Khóa từ CP4):**
  > *"Đạt khi $\ge 85\%$ Precision, $\ge 90\%$ Recall trên bộ Golden set 20 case, và không bỏ sót bất kỳ câu hỏi nào tồn đọng trên 4 tiếng."*
- **Kết quả các lượt chạy:** Sẽ cập nhật bảng đo lường sau khi chạy kiểm thử AI tại CP3.

---

## §8. Phân công & Kế hoạch

- **Phân công chi tiết:**
  - **Nguyễn Thái Anh (2A202602810):** Thiết kế Spec (§1, §4, §6), xây dựng Sơ đồ luồng (`flow.md`) và lập trình bản Prototype tương tác (`codebase/prototype/index.html`).
  - **Hoàng Ngọc Đăng Khoa (2A202602790):** Khảo sát người dùng, thu thập bằng chứng thực tế, phân tích dữ liệu khảo sát và viết phần Impact (§1, §2).
  - **Ngọ Doãn Ngọc:** Xây dựng bộ dữ liệu kiểm thử Golden set (20 case) và thiết kế prompt phân loại / gom cụm cho CP3.
  - **Đoàn Quang Minh:** Chạy kiểm thử đo lường đánh giá prompt, chuẩn bị kịch bản quay video demo CP3 và slide pitch CP5.
- **Willing users (≥2 tên từ khảo sát thực tế):**
  1. *TA 1 (Timestamp 16/9 19:14:28):* Tồn đọng 6–10h, mất thời gian research & dò thủ công — Xác nhận sẵn sàng dùng thử.
  2. *TA 2 (Timestamp 16/9 19:16:20):* Mất 10p cuộn chuột, quá nhiều tin phải đọc hết — Xác nhận sẵn sàng dùng thử.
  3. *TA 3 (Timestamp 16/9 19:17:23):* Kỷ lục tồn 7h khi ốm, khó nắm bắt tình hình — Xác nhận sẵn sàng dùng thử.
  4. *TA 4 (Timestamp 16/9 20:29:37):* Kỷ lục tồn 24h, mất 60p cuộn chuột/ngày, 50% câu hỏi trùng lặp — Xác nhận sẵn sàng dùng thử.
  5. *TA 5 (Timestamp 17/9 10:14:19):* Mất 30–45p cuộn chuột/ngày, đợi load lâu rối mắt — Xác nhận sẵn sàng dùng thử.
  6. *TA 6 (Timestamp 17/9 10:15:35):* Kỷ lục tồn 4h, mất 15p lướt thủ công bằng tay — Xác nhận sẵn sàng dùng thử.
- **Multi-prototype:**
  - Phương án A: Xem theo dòng thời gian (FIFO Queue) — Tập trung giải cứu ca tồn lâu nhất.
  - Phương án B: Xem theo phân cụm chủ đề (Clustering) — Tập trung giải quyết dứt điểm các câu hỏi lặp lại.
  - ➔ Cả 2 phương án đã được tích hợp song song trong cùng 1 giao diện prototype để TA tùy chọn theo ngữ cảnh trực.

---

## §9. Changelog

| Thời điểm | Đổi gì | Vì sao (Trỏ về feedback / case nào) |
|---|---|---|
| 16/9 19:30 | Hoàn thành Canvas CP1 & thu thập khảo sát $n=10$ | Khóa mục tiêu bài toán Track B2 dựa trên nỗi đau thực tế của TA |
| 16/9 20:30 | Tạo `docs/flow.md` và `codebase/prototype/index.html` | Thiết kế luồng 1-Click Jump và bản mock tương tác chuẩn Discord |
| 16/9 20:45 | Thêm nút Reload và Limit 15 câu/popup | Tránh quá tải thông tin và hỗ trợ TA quét lại dữ liệu realtime |
| 17/9 10:30 | Cập nhật toàn diện `spec.md` cho CP2 | Bổ sung chi tiết §4, §6, 4 nguyên tắc HAX/PAIR theo yêu cầu CP2 |
| 17/9 19:45 | Chuẩn hóa số liệu khảo sát $n=10$ (16–17/9) | Đồng bộ kỷ lục tồn 24h, thời gian lội kênh 15–60p, 50% câu trùng, mở rộng 6 Willing Users |
