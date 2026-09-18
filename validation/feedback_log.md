# Nhật Ký Dùng Thử Sản Phẩm (User Validation Log) — Bonus R6
> **Dự án:** Track B2 — Triage Hub `/remaining-questions`  
> **Nhóm:** Phronesis · Lớp K4-3A · Phòng E403  
> **Phương pháp thử nghiệm:** 5 nhịp kiểm thử người dùng độc lập (Comfort ➔ Context ➔ Task ➔ Observe ➔ Post-interview) theo chuẩn Stanford CS177 / Sean Ellis Disappointment Score.

---

## 1. Bảng Nhật Ký Kiểm Thử Với Người Dùng Ngoài Nhóm (n = 3)

| Người thử | Vai trò & Bối cảnh | Task giao cho người thử | Hành vi quan sát được (Observe) | Quote nguyên văn từ người dùng | Mức độ nghiêm trọng & Phản hồi |
|---|---|---|---|---|---|
| **Lê Đức Anh** | Lab Coach ca trực tối (Phòng E401, ngoài nhóm) · *Willing User* | *"Bạn hãy tìm xem có học viên nào đang bị kẹt lỗi kỹ thuật chưa được trả lời trong ca trực không và xử lý."* | - Ban đầu quen tay cuộn chuột lướt tìm.<br>- Được nhắc dùng lệnh ➔ gõ `/rem` ➔ thấy popup lệnh.<br>- Nhấn Enter ➔ mắt nhìn ngay vào badge đỏ URGENT.<br>- Click vào thẻ ➔ màn hình nhảy ngay đến tin nhắn gốc. | *"Ủa tiện thế! Bấm một cái nó cuộn đúng đến tin lỗi OPA luôn, không phải lội ngược 300 tin nữa. Viền vàng nhấp nháy dễ nhìn."* | **Thành công (Tích cực).** Gợi ý: *"Nên có thêm số phút học viên đã chờ để biết ca nào sắp chạm trần."* |
| **Trần Thu Trang** | Trợ giảng trực Discord (Lớp 3B, ngoài nhóm) · *Willing User* | *"Hãy kiểm tra các thắc mắc về điểm danh hoặc quy chế thi và phản hồi học viên."* | - Chuyển sang kênh `#hỏi-đáp-logistics`.<br>- Gõ `/remaining-questions` ➔ mở tab **📁 Theo Chủ Đề**.<br>- Chọn nhóm *Logistics & Chuyên cần* ➔ click vào câu hỏi điểm danh bù của T050.<br>- Đọc phần giải thích AI rồi mở portal đối soát. | *"Hay ở chỗ bot không tự phán bừa là em đã điểm danh hay chưa. Điểm danh là việc nhạy cảm, bot dẫn link để mình tự tra cứu thế này là chuẩn nhất."* | **Thành công (Tích cực).** Rất thích cơ chế Augment không hallucinate. |
| **Nguyễn Văn Hùng** | TA phòng E402 (ngoài nhóm) · Người có kỷ lục sót tin 24h | *"Hãy rà soát xem có tin nhắn rác hoặc spam nào làm phiền hàng đợi của bạn không."* | - Thử gõ lệnh ở kênh `#thảo-luận-chung` (toàn tin ăn trưa).<br>- Bot trả về: *'0 câu hỏi tồn đọng'*, không hiện danh sách rác.<br>- Thử bấm vào case phân mảnh của bạn Đức ở kênh Lab ➔ thấy 3 tin ngắn sáng cùng lúc. | *"Ban đầu sợ bot lại bốc mấy tin rủ đi ăn trưa vào thì rác lắm, nhưng quét ra 0 tin là ngon. Gộp được 3 tin nhắn rời của 1 người làm một là cứu cánh thực sự."* | **Thành công (Tích cực).** Đánh giá cao khả năng lọc nhiễu. |

---

## 2. Điểm Đánh Giá Mức Độ Thất Vọng (Sean Ellis Disappointment Test)
- **Câu hỏi:** *"Nếu từ ngày mai không được sử dụng lệnh `/remaining-questions` nữa, bạn sẽ cảm thấy thế nào?"*
  - **3/3 người thử nghiệm (100%)** trả lời: **"Rất tiếc (Very disappointed)"** vì lại phải quay về cảnh lội kênh thủ công mất 20–30 phút mỗi ca trực.

---

## 3. Tổng Hợp Đóng Góp & Những Thay Đổi Đã Thực Hiện (Vào Changelog Spec §9)

1. **Thay đổi đã làm ngay trước Demo:**
   - **Gắn nhãn thời gian chờ cụ thể (`⏳ Tồn 11h45p`, `⏳ Tồn 45p`):** Theo phản hồi của anh Đức Anh để TA biết chính xác ca nào đang sát ngưỡng kỷ lục tồn đọng.
   - **Bổ sung hiệu ứng làm nổi bật đa tin nhắn (`relatedIds`):** Khi bấm vào câu hỏi phân mảnh, toàn bộ cụm 3 tin nhắn rời rạc đều phát sáng viền vàng để TA đọc đủ ngữ cảnh.
   - **Giữ nguyên 100% dạng tin nhắn riêng tư (Ephemeral Message):** Không đăng công khai hàng đợi lên kênh chung để bảo mật thông tin cá nhân (MSSV, lý do vắng học) của học viên.
2. **Đưa vào Backlog (Kế hoạch tuần tới):**
   - Tích hợp thêm nút bấm *"Đã giải quyết"* trực tiếp trên tin nhắn Discord để tự động xóa khỏi hàng đợi Redis mà không cần chờ lượt quét định kỳ.
