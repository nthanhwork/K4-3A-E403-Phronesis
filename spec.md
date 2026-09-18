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
- **Evidence (Chuẩn A Khảo sát & Chuẩn B Data Mining kiểm chứng được — Log đầy đủ trong repo):**
  - *Chuẩn A — Khảo sát thực tế ($n = 10$ TA/Lab Coach thực tế ngày 16–17/9/2026):*
    - **90% (9/10 TA)** xác nhận mất thời gian mỗi ngày chỉ để cuộn chuột lội kênh tìm câu hỏi (thời gian cuộn từ 10 đến 60 phút/ngày, trung bình ~22 phút/ngày).
    - **Kỷ lục câu hỏi bị tồn đọng:** Lên tới **24 tiếng** (TA mốc 20:29), **12 tiếng** (TA mốc 19:13), **6–10 tiếng** (TA mốc 19:14), **7 tiếng** (TA mốc 19:17 do bị ốm), và **4 tiếng** (TA mốc 10:15).
    - **Tỷ lệ trùng lặp:** **13% – 50%** (hoặc 20–30 câu hỏi lặp lại/ngày), khiến TA nản lòng dẫn đến xử lý bằng cách *"bỏ qua luôn"* hoặc phải trả lời đi trả lời lại.
    - **60% (6/10 TA)** sẵn sàng tham gia dùng thử giải pháp mới ngay lập tức.
  - *Chuẩn B — Data Mining thực tế từ `data/discord-pack/k4_messages.csv` (1.092 tin nhắn):*
    - **Tổng số tin nhắn trích xuất:** 1.092 tin nhắn từ ngày 12/9 đến 16/9/2026.
    - **Số câu hỏi kỹ thuật/thủ tục của học viên:** 136 tin nhắn (12.5% tổng lưu lượng).
    - **Tỷ lệ câu hỏi không có người phản hồi sau > 2 giờ:** 52/136 tin nhắn (**38.2%**).
    - **Kỷ lục tồn đọng thực tế trong chatlog:** **12 giờ 25 phút** (tin nhắn `M63574` từ học viên D3082).
    - **Tỷ lệ câu hỏi trùng lặp nội dung:** 31/136 tin nhắn (**22.8%**) tập trung vào: quy chế sĩ số team, lỗi cài đặt CVAT, lỗi OPA Docker Compose.
    - *Phương pháp đếm kiểm chứng lại được (Reproducible Counting Method):* Dùng script Python lọc toàn bộ tin nhắn `is_bot != 'True'`, tìm kiếm regex dấu hỏi `?` hoặc các từ khóa hỗ trợ ("cho em hỏi", "lỗi", "giúp em", "sửa sao"), sau đó đối soát timestamp `created_at_vn` với tin nhắn phản hồi đầu tiên của Lab Coach.
  - *≥5 Quote nguyên văn từ người dùng thật trong chatlog và khảo sát:*
    1. *"A ơi, cho e hỏi, buổi workshop chủ nhật ngày mai thì có tính vào số buổi nghỉ ko ạ? Giả dụ sáng mai e có việc..."* — Học viên D3082 (Tin nhắn `M63574`, chờ 12h25p)
    2. *"T3 tuần sau lecture sáng em có việc muốn xin vào trễ 30p thì gửi mail cho a [HV] ạ?"* — Học viên D7482 (Tin nhắn `M56857`, chờ 6h30p)
    3. *"chào bạn Ngay sau docker compose up -d, OPA chưa lấy được policy bundle từ cvat-server, nên health check báo: OPA service unhealthy. Mình đã kiểm tra network nhưng chưa fix được."* — Học viên D6587 (Tin nhắn `M12802`, lỗi kỹ thuật chờ hỗ trợ)
    4. *"cho mình hỏi một team bao nhiêu bạn ?"* — Học viên D1224 (Tin nhắn `M83358`, câu hỏi trùng lặp sĩ số)
    5. *"Hi, mình vẫn chưa cài được CVAT. Có bạn nào hỗ trợ được mình không?"* — Học viên D5159 (Tin nhắn `M07901`, kêu cứu cài đặt môi trường)
    6. *"Quá nhiều tin mà phải đọc hết"* & *"Bị trôi tin nhắn"* — TA Khảo sát thực tế (Timestamp 19:16:20 & 19:18:21)
    7. *"Khó khăn khi cuộn chuột, nhiều text. Tìm bằng ctrl F nhưng phải cuộn đến gần vùng đó"* & *"Phải lướt thủ công để tìm, lướt bằng tay"* — TA Khảo sát thực tế (Timestamp 19:47:00 & 10:15:35)

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

| Lớp taxonomy chỗ khó | Tình huống / Kịch bản cụ thể | Hệ thống xử lý thế nào để tránh fail (Desired Behavior) |
|---|---|---|
| **① Nguồn sự thật** *(hallucination / đoán mò)* | Học viên hỏi điểm danh cá nhân (TC14): *"em không nhớ mình đã điểm danh ra về chưa, MSSV 2A202602819"* | AI **tuyệt đối không bịa** kết quả điểm danh; hệ thống phân loại vào cụm `Logistics & Chuyên cần`, mức `urgent` và dẫn link để TA tra cứu danh sách thực tế. |
| **① Nguồn sự thật** *(hallucination / đoán mò)* | Học viên thắc mắc quy chế chấm nộp bài GitHub Classroom (TC26: clone code vs fork) | AI không tự phán xét đúng/sai; gán nhãn câu hỏi kỹ thuật cần TA đối soát rubric chính thức của BTC để giải đáp chuẩn xác. |
| **② Mơ hồ / Thiếu thông tin** *(câu hỏi cộc lốc)* | Học viên gọi mentor cộc lốc tại phòng học (TC17, TC38): *"anh ơi tới zone 2 giúp em"* hoặc *"lỗi rồi"* | AI nhận diện đây là lời kêu cứu kỹ thuật khẩn cấp (`urgent`), không suy đoán lỗi mà giữ nguyên trích đoạn và số bàn để TA đến hỗ trợ trực tiếp. |
| **② Mơ hồ / Thiếu thông tin** *(câu hỏi cộc lốc)* | Học viên gửi báo lỗi không kèm mã lỗi (TC27): *"em chạy tới bước 3 thì bị lỗi như này ạ"* | AI xếp vào `Kỹ thuật & Bài Lab`, mức `medium`, hiển thị trích đoạn kèm link 1-Click Jump để TA nhảy đến yêu cầu cung cấp log chi tiết. |
| **③ Ngoài phạm vi / Thẩm quyền** *(làm bài hộ / lạc đề)* | Học viên nhờ làm bài hộ (TC18): *"bạn code giải hộ mình câu 3 với câu 4 nộp giúp mình luôn với"* | AI nhận diện đây là câu hỏi cần can thiệp để TA vào nhắc nhở quy chế liêm chính học thuật, không bao giờ sinh lời giải thay học viên. |
| **③ Ngoài phạm vi / Thẩm quyền** *(làm bài hộ / lạc đề)* | Tin nhắn rủ đi ăn trưa (TC20) hoặc hỏi đồ án trường khác (TC39) | AI lọc bỏ hoàn toàn (`is_unanswered_question=False`) hoặc gắn nhãn ngoài phạm vi để tránh làm rác hàng đợi của TA. |
| **④ Đặc thù nghiệp vụ** *(thread con / spam lặp)* | 1 học viên gửi liên tiếp 4 tin nhắn trong 5 phút để mô tả 1 lỗi kỹ thuật | Heuristic gom nhóm các tin nhắn liên tiếp của cùng 1 User thành 1 item duy nhất trong hàng đợi, tránh tạo rác phân mảnh. |
| **④ Đặc thù nghiệp vụ** *(thread con / spam lặp)* | Nhiều học viên hỏi cùng 1 câu ở các kênh khác nhau (TC04, TC05, TC33: sĩ số team) | Thuật toán phân cụm gom tất cả vào nhóm `Khảo sát & Nhóm` để TA chỉ cần trả lời 1 lần chung cho cả lớp. |
| **④ Đặc thù nghiệp vụ** *(thread con / spam lặp)* | Tin nhắn thông báo từ BTC (TC11, TC37) hoặc emoji vui đùa (TC13) | AI phân loại `is_unanswered_question=False`, loại bỏ 100% khỏi hàng đợi để giữ hàng đợi tinh gọn, sạch sẽ. |
| **Edge cases** *(tấn công phá hoại)* | Prompt injection (TC19, TC40): Cố tình chèn lệnh override system rules hoặc drop database | Hệ thống coi toàn bộ tin nhắn học viên là dữ liệu thuần (Untrusted Data), không bao giờ thực thi chỉ thị, trả về `is_unanswered_question=False`. |

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

- **Chiều chất lượng + Định nghĩa kiểm chứng được (Người ngoài nhóm chấm ra cùng kết quả):**
  - *1. Triage Precision (Độ chuẩn xác lọc câu hỏi):* Tỷ lệ các tin nhắn được AI gán nhãn là câu hỏi thực sự là câu hỏi cần TA hỗ trợ.
    $$\text{Precision} = \frac{TP}{TP + FP} = \frac{\text{Số ca AI đoán là câu hỏi VÀ đúng là câu hỏi}}{\text{Tổng số ca AI dự đoán là câu hỏi}}$$
  - *2. Triage Recall (Độ bao phủ câu hỏi):* Tỷ lệ các câu hỏi thực tế của học viên được AI phát hiện thành công, không bị bỏ lọt.
    $$\text{Recall} = \frac{TP}{TP + FN} = \frac{\text{Số câu hỏi thực tế được AI phát hiện}}{\text{Tổng số câu hỏi thực tế trong tập test}}$$
  - *3. Topic Clustering Accuracy (Độ chính xác gom cụm chủ đề):* Tỷ lệ gán đúng 1 trong 4 nhóm chủ đề nghiệp vụ chuẩn (*Kỹ thuật & Bài Lab, Logistics & Chuyên cần, Khảo sát & Nhóm, Ngoài phạm vi*).
  - *4. Urgency Calibration Accuracy (Độ chuẩn xác mức khẩn cấp):* Tỷ lệ gán đúng mức ưu tiên hỗ trợ (*urgent, medium, low, none*).
  - *5. Full Match Rate (Tỷ lệ đạt chuẩn toàn diện cả 3 trường):* Tỷ lệ các ca mà AI khớp đồng thời cả 3 trường thông tin: Triage, Topic và Urgency.

- **Bộ dữ liệu kiểm thử Golden Set (40 test cases nhóm tự xây — `eval/golden_set.json`):**
  - **Quy mô:** Đạt **40 trường hợp kiểm thử độc lập** (vượt xa mức tối thiểu 20 ca của rubric).
  - **Cơ cấu taxonomy:**
    - *① Nguồn sự thật:* 5 ca (TC14, TC15, TC21, TC23, TC26) — thắc mắc điểm danh, app lỗi thẻ, quy chế clone/fork lab.
    - *② Mơ hồ / Thiếu thông tin:* 4 ca (TC16, TC17, TC27, TC38) — câu hỏi cộc lốc "anh ơi", "tới zone 2", lỗi không kèm log.
    - *③ Ngoài phạm vi / Thẩm quyền:* 3 ca (TC18, TC20, TC39) — nhờ giải bài hộ, rủ ăn trưa, hỏi bài thi trường ngoài.
    - *④ Đặc thù nghiệp vụ:* 8 ca (TC05, TC11, TC12, TC13, TC33, TC35, TC36, TC37) — spam emoji, trùng lặp sĩ số team, thông báo BTC, reply cảm ơn.
    - *Phổ biến hàng ngày:* 18 ca (TC01-TC04, TC06-TC10, TC22, TC24, TC25, TC28-TC32, TC34) — các câu hỏi lặp lại thường nhật.
    - *Hiếm gặp / Edge cases:* 2 ca (TC19, TC40) — các đợt tấn công prompt injection phá hoại DB hoặc phá vỡ format JSON.
  - **Nguồn gốc dữ liệu thật:** **34/40 ca (85%)** được trích xuất trực tiếp từ chatlog thật `data/discord-pack/k4_messages.csv` và phòng học thực tế E403 (vượt xa chỉ tiêu $\ge 10$ ca của rubric).

- **Quality Bar (Khóa từ CP4, mốc 21:00 17/9 — giữ nguyên sau đó):**
  > *"Hệ thống đạt chuẩn nghiệm thu khi: Precision $\ge 85.0\%$, Recall $\ge 90.0\%$ (tuyệt đối không bỏ sót câu hỏi tồn đọng $> 2$ tiếng, tức $FN = 0$), Topic Clustering Accuracy $\ge 80.0\%$, Urgency Accuracy $\ge 60.0\%$, Full Match $\ge 50.0\%$, và Độ trễ phản hồi trung bình $\le 3.0\text{s}$ trên trọn bộ 40 test cases của Golden Set."*

- **Bảng kết quả chạy kiểm thử thực tế (Run 1 — Đo lường trên model `gpt-4o-mini`):**
  *(Trích từ `eval/run_results.md`, kèm 125 tệp log JSON đối soát trong `eval/logs/`)*

  | Tiêu chí chất lượng | Kết quả thực tế (Run 1) | Quality Bar cam kết | Trạng thái nghiệm thu |
  | :--- | :---: | :---: | :---: |
  | **Triage Accuracy (Lọc câu hỏi)** | **100.0%** (40/40) | $\ge 85.0\%$ | ✅ **VƯỢT CHỈ TIÊU** |
  | **Precision** | **100.0%** (31/31) | $\ge 85.0\%$ | ✅ **ĐẠT** |
  | **Recall (Không bỏ sót)** | **100.0%** (31/31, $FN=0$) | $\ge 90.0\%$ | ✅ **ĐẠT TUYỆT ĐỐI** |
  | **F1-Score** | **100.0%** | $\ge 85.0\%$ | ✅ **ĐẠT** |
  | **Topic Clustering Accuracy** | **92.5%** (37/40) | $\ge 80.0\%$ | ✅ **ĐẠT** |
  | **Urgency Calibration Accuracy** | **60.0%** (24/40) | $\ge 60.0\%$ | ✅ **ĐẠT** |
  | **Full Match (Khớp trọn vẹn 3 trường)** | **57.5%** (23/40) | $\ge 50.0\%$ | ✅ **ĐẠT** |
  | **Độ trễ trung bình (Latency)** | **1.60s** / request | $\le 3.0\text{s}$ | ✅ **ĐẠT** |

- **Tự khai báo các hạng mục chưa kịp xử lý trong đợt chạy hiện tại (Self-declaration of Unfinished Items):**
  1. *Hiệu chuẩn mức độ khẩn cấp (Urgency Calibration) mới đạt 60.0% (24/40 ca):* Dù đã đạt ngưỡng sàn cam kết ($\ge 60\%$), mô hình vẫn có xu hướng hạ mức ưu tiên từ `urgent` xuống `medium`/`low` đối với các câu hỏi học viên dùng ngôn từ lịch sự ("em chào anh", "nhờ anh chị hỗ trợ chút") dù vấn đề phát sinh ngay trước deadline hoặc sát giờ vào lớp. Nhóm đã xác định giải pháp bổ sung few-shot in-context learning ở Run 2 (CP5) để nâng tỷ lệ này lên $\ge 75\%$.
  2. *Gom cụm câu hỏi giao thoa đa chủ đề (Multi-label Overlap):* Có 3 ca (TC03, TC04, TC33) liên quan đến deadline ghép nhóm bị mô hình phân loại vào `Logistics & Chuyên cần` thay vì `Khảo sát & Nhóm` do câu hỏi chứa cả mốc thời gian lẫn việc ghép đội. Hiện tại mô hình chỉ gán 1 nhãn duy nhất (single-label), chưa hỗ trợ cơ chế đa nhãn (multi-label tagging).
  3. *Tự động hợp nhất tin nhắn phân mảnh ở Backend:* Tính năng nhóm các tin nhắn spam hoặc gửi rời rạc trong vòng 5 phút của cùng một học viên hiện mới được hiện thực hóa ở tầng giao diện Prototype, chưa xây dựng pipeline Redis sliding-window session trên server backend để gom nhóm tự động trước khi đẩy vào prompt LLM.
  4. *Triển khai Bot Discord trực tiếp lên Gateway Production:* Hệ thống hiện hoạt động ổn định ở cấp độ **Working Prototype** (Web Prototype tương tác chuẩn giao diện Discord + Backend API Server Python kết nối trực tiếp OpenAI `gpt-4o-mini`). Việc triển khai bot chạy 24/7 trực tiếp trên máy chủ Discord chính thức của VinUni đòi hỏi phân quyền quản trị từ Ban tổ chức, do đó được xếp vào kế hoạch triển khai sau hackathon.

---

## §8. Phân công & Kế hoạch

- **Phân công chi tiết:**
  - **Nguyễn Thái Anh (2A202602810) — Lead Developer & System Architect:** Thiết kế Spec kỹ thuật (§1, §4, §6), xây dựng sơ đồ luồng `docs/flow.md`, phát triển Core AI Engine (`codebase/triage_engine.py`), Server live (`codebase/server.py`), kịch bản demo (`codebase/live_demo.py`) và quản trị Git.
  - **Ngọ Doãn Ngọc (2A202602635) — Team Leader & Product Manager:** Điều phối tiến độ tổng thể, đại diện nhóm nộp Form các mốc CP1–CP5, thiết kế Prompt System cho Triage Hub, định nghĩa tiêu chí nghiệm thu và review chất lượng sản phẩm.
  - **Hoàng Ngọc Đăng Khoa (2A202602790) — Data Analyst & Evaluation Specialist:** Khai phá dữ liệu chatlog `data/discord-pack/k4_messages.csv`, xây dựng bộ dữ liệu kiểm thử Golden Set 40 cases (§7), thực thi script đánh giá `eval/run_eval.py` và phân tích lỗi `eval/run_results.md`.
  - **Đoàn Quang Minh (2A202602711) — Media Lead & UX Validation:** Phụ trách quay video demo 30s thực tế, kiểm thử trải nghiệm giao diện người dùng theo 5 nguyên tắc HAX/PAIR, xây dựng kịch bản trình chiếu slide demo CP5 và phản biện vòng CP6.
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
- **Kế hoạch kiểm thử và tinh chỉnh thực tế (Thực hiện cho CP5):**
  1. *Kế hoạch Prompt Iteration (Run 2):* Bổ sung 3 few-shot examples vào `SYSTEM_PROMPT` trong `codebase/triage_engine.py` để hướng dẫn mô hình nhận diện yếu tố khẩn cấp dựa trên tính chất công việc thay vì chỉ dựa vào từ khóa ngữ nghĩa bề mặt.
  2. *Đo lường kiểm chứng lại:* Tái thực thi toàn bộ 40 test cases qua `eval/run_eval.py`, ghi nhận log và cập nhật bảng so sánh Run 1 vs Run 2 để chứng minh tính cải tiến liên tục trước Ban giám khảo.
  3. *Đóng gói bài thuyết trình (Pitch Deck CP5):* Hoàn thiện 5 slide thuyết trình tập trung vào: Bằng chứng người dùng (Data mining 1.092 tin) ➔ Demo tương tác 30s ➔ Đo lường độ tin cậy AI với 40 cases ➔ Kế hoạch hoàn thiện.

---

## §9. Changelog

| Thời điểm | Đổi gì | Vì sao (Trỏ về feedback / case nào) |
|---|---|---|
| 16/9 19:30 | Hoàn thành Canvas CP1 & thu thập khảo sát $n=10$ | Khóa mục tiêu bài toán Track B2 dựa trên nỗi đau thực tế của TA |
| 16/9 20:30 | Tạo `docs/flow.md` và `codebase/prototype/index.html` | Thiết kế luồng 1-Click Jump và bản mock tương tác chuẩn Discord |
| 16/9 20:45 | Thêm nút Reload và Limit 15 câu/popup | Tránh quá tải thông tin và hỗ trợ TA quét lại dữ liệu realtime |
| 17/9 19:45 | Chuẩn hóa số liệu khảo sát $n=10$ (16–17/9) | Đồng bộ kỷ lục tồn 24h, thời gian lội kênh 15–60p, 50% câu trùng, mở rộng 6 Willing Users |
| 17/9 20:45 | Khóa Quality Bar CP4 & tự khai báo các khuyết điểm | Đóng băng ngưỡng chất lượng định lượng, bổ sung tự khai báo các phần chưa xong và kế hoạch cho CP5 |
| 18/9 10:30 | Thử nghiệm người dùng ngoài nhóm ($n=5$) & Hoàn thành Bonus R6 | Kiểm thử usability với 5 học viên K4 (02706, 02782, 02903, 02682, 02728); cập nhật `validation/feedback_log.md`; sẽ cân nhắc tinh chỉnh thời gian highlight Jump Link, loading spinner và độ tương phản badge |
