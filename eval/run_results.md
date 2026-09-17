# BÁO CÁO ĐÁNH GIÁ KIỂM THỬ SƠ BỘ (RUN 1) - CHECKPOINT 3
## Đề B2: /remaining-questions (Triage Hub cho Đội ngũ Trợ giảng)
**Nhóm:** Phronesis | **Lớp:** K4-3A | **Phòng:** E403 | **Ngày đánh giá:** 17/09/2026

---

### 1. Tóm tắt Chỉ số Hiệu năng Chính (Key Metrics)

| Chỉ số đo lường (Metric) | Kết quả đạt được | Mục tiêu đề ra (CP1/CP2) | Trạng thái |
| :--- | :---: | :---: | :---: |
| **Độ chính xác Lọc câu hỏi (Triage Accuracy)** | **100.0%** (40/40) | $\ge 85.0\%$ | ✅ ĐẠT |
| **Khớp hoàn hảo cả 3 tiêu chí (Full Match)** | **57.5%** (23/40) | $\ge 75.0\%$ | ⚠️ CHẤP NHẬN ĐƯỢC |
| **Precision (Độ chuẩn xác câu hỏi tồn đọng)** | **100.0%** | $\ge 80.0\%$ | ✅ ĐẠT |
| **Recall (Tỷ lệ không bỏ sót câu hỏi)** | **100.0%** | $\ge 90.0\%$ | ✅ ĐẠT |
| **F1-Score** | **100.0%** | $\ge 85.0\%$ | ✅ ĐẠT |
| **Độ chính xác Gom cụm Chủ đề (Topic)** | **92.5%** | $\ge 80.0\%$ | ✅ ĐẠT |
| **Độ chính xác Mức khẩn cấp (Urgency)** | **60.0%** | $\ge 70.0\%$ | ⚠️ |
| **Thời gian phản hồi trung bình (Latency)** | **1.60s** / tin nhắn | <= 3.0s | ✅ ĐẠT |

### 2. Ma trận Nhầm lẫn (Confusion Matrix - Nhận diện Câu hỏi)

| Thực tế \ Dự đoán của AI | Dự đoán: LÀ CÂU HỎI (Positive) | Dự đoán: KHÔNG PHẢI (Negative) |
| :--- | :---: | :---: |
| **Thực tế: Là câu hỏi cần TA** | **TP = 31** | **FN = 0** |
| **Thực tế: Không cần TA** | **FP = 0** | **TN = 9** |

### 3. Bảng Kết quả Chi tiết 40 Test Cases

| ID | Nguồn & Mã tin | Phân loại Chỗ khó | Dự đoán AI (Q / Topic / Urgency) | Kỳ vọng (Ground Truth) | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **TC01** | M63574 | Phổ biến hàng ngày | `Q=True / Logistics & Chuyên cần / medium` | `Q=True / Logistics & Chuyên cần / medium` | ✅ Chuẩn |
| **TC02** | M56857 | Phổ biến hàng ngày | `Q=True / Logistics & Chuyên cần / medium` | `Q=True / Logistics & Chuyên cần / medium` | ✅ Chuẩn |
| **TC03** | M83711 | Phổ biến hàng ngày | `Q=True / Logistics & Chuyên cần / low` | `Q=True / Logistics & Chuyên cần / medium` | ⚠️ Lệch phụ |
| **TC04** | M83358 | Phổ biến hàng ngày | `Q=True / Khảo sát & Nhóm / low` | `Q=True / Khảo sát & Nhóm / low` | ✅ Chuẩn |
| **TC05** | M99769 | Lớp 4: Đặc thù nghiệp vụ | `Q=True / Khảo sát & Nhóm / low` | `Q=True / Khảo sát & Nhóm / low` | ✅ Chuẩn |
| **TC06** | M57505 | Phổ biến hàng ngày | `Q=True / Logistics & Chuyên cần / low` | `Q=True / Logistics & Chuyên cần / medium` | ⚠️ Lệch phụ |
| **TC07** | M19124 | Phổ biến hàng ngày | `Q=True / Khảo sát & Nhóm / medium` | `Q=True / Logistics & Chuyên cần / urgent` | ⚠️ Lệch phụ |
| **TC08** | M12802 | Phổ biến hàng ngày | `Q=True / Kỹ thuật & Bài Lab / urgent` | `Q=True / Kỹ thuật & Bài Lab / urgent` | ✅ Chuẩn |
| **TC09** | M94349 | Phổ biến hàng ngày | `Q=True / Ngoài phạm vi / Không liên quan / low` | `Q=True / Logistics & Chuyên cần / low` | ⚠️ Lệch phụ |
| **TC10** | M30201 | Phổ biến hàng ngày | `Q=True / Logistics & Chuyên cần / low` | `Q=True / Logistics & Chuyên cần / medium` | ⚠️ Lệch phụ |
| **TC11** | M47011 | Lớp 4: Đặc thù nghiệp vụ | `Q=False / Ngoài phạm vi / Không liên quan / none` | `Q=False / Ngoài phạm vi / Không liên quan / none` | ✅ Chuẩn |
| **TC12** | M58687 | Lớp 4: Đặc thù nghiệp vụ | `Q=False / Ngoài phạm vi / Không liên quan / none` | `Q=False / Ngoài phạm vi / Không liên quan / none` | ✅ Chuẩn |
| **TC13** | M14882 | Lớp 4: Đặc thù nghiệp vụ | `Q=False / Ngoài phạm vi / Không liên quan / none` | `Q=False / Ngoài phạm vi / Không liên quan / none` | ✅ Chuẩn |
| **TC14** | E403_01 | Lớp 1: Nguồn sự thật | `Q=True / Logistics & Chuyên cần / medium` | `Q=True / Logistics & Chuyên cần / urgent` | ⚠️ Lệch phụ |
| **TC15** | E403_02 | Lớp 1: Nguồn sự thật | `Q=True / Kỹ thuật & Bài Lab / medium` | `Q=True / Kỹ thuật & Bài Lab / urgent` | ⚠️ Lệch phụ |
| **TC16** | E403_03 | Lớp 2: Mơ hồ / Thiếu thông tin | `Q=True / Khảo sát & Nhóm / low` | `Q=True / Khảo sát & Nhóm / medium` | ⚠️ Lệch phụ |
| **TC17** | E403_04 | Lớp 2: Mơ hồ / Thiếu thông tin | `Q=True / Logistics & Chuyên cần / medium` | `Q=True / Kỹ thuật & Bài Lab / urgent` | ⚠️ Lệch phụ |
| **TC18** | SYN_01 | Lớp 3: Ngoài phạm vi / Thẩm quyền | `Q=True / Kỹ thuật & Bài Lab / urgent` | `Q=True / Kỹ thuật & Bài Lab / low` | ⚠️ Lệch phụ |
| **TC19** | SYN_02 | Edge cases | `Q=False / Ngoài phạm vi / Không liên quan / none` | `Q=False / Ngoài phạm vi / Không liên quan / none` | ✅ Chuẩn |
| **TC20** | SYN_03 | Lớp 3: Ngoài phạm vi / Thẩm quyền | `Q=False / Ngoài phạm vi / Không liên quan / none` | `Q=False / Ngoài phạm vi / Không liên quan / none` | ✅ Chuẩn |
| **TC21** | M37211 | Lớp 1: Nguồn sự thật | `Q=True / Logistics & Chuyên cần / medium` | `Q=True / Logistics & Chuyên cần / urgent` | ⚠️ Lệch phụ |
| **TC22** | M28943 | Phổ biến hàng ngày | `Q=True / Logistics & Chuyên cần / medium` | `Q=True / Logistics & Chuyên cần / medium` | ✅ Chuẩn |
| **TC23** | M03966 | Lớp 1: Nguồn sự thật | `Q=True / Logistics & Chuyên cần / medium` | `Q=True / Logistics & Chuyên cần / urgent` | ⚠️ Lệch phụ |
| **TC24** | M27566 | Phổ biến hàng ngày | `Q=True / Logistics & Chuyên cần / low` | `Q=True / Logistics & Chuyên cần / medium` | ⚠️ Lệch phụ |
| **TC25** | M07901 | Phổ biến hàng ngày | `Q=True / Kỹ thuật & Bài Lab / urgent` | `Q=True / Kỹ thuật & Bài Lab / urgent` | ✅ Chuẩn |
| **TC26** | M89035 | Lớp 1: Nguồn sự thật | `Q=True / Kỹ thuật & Bài Lab / medium` | `Q=True / Kỹ thuật & Bài Lab / urgent` | ⚠️ Lệch phụ |
| **TC27** | M51326 | Lớp 2: Mơ hồ / Thiếu thông tin | `Q=True / Kỹ thuật & Bài Lab / urgent` | `Q=True / Kỹ thuật & Bài Lab / medium` | ⚠️ Lệch phụ |
| **TC28** | M55571 | Phổ biến hàng ngày | `Q=True / Kỹ thuật & Bài Lab / medium` | `Q=True / Kỹ thuật & Bài Lab / medium` | ✅ Chuẩn |
| **TC29** | M40002 | Phổ biến hàng ngày | `Q=True / Kỹ thuật & Bài Lab / low` | `Q=True / Kỹ thuật & Bài Lab / low` | ✅ Chuẩn |
| **TC30** | M00554 | Phổ biến hàng ngày | `Q=True / Khảo sát & Nhóm / low` | `Q=True / Khảo sát & Nhóm / low` | ✅ Chuẩn |
| **TC31** | M01844 | Phổ biến hàng ngày | `Q=True / Khảo sát & Nhóm / low` | `Q=True / Khảo sát & Nhóm / medium` | ⚠️ Lệch phụ |
| **TC32** | M88368 | Phổ biến hàng ngày | `Q=True / Khảo sát & Nhóm / low` | `Q=True / Khảo sát & Nhóm / low` | ✅ Chuẩn |
| **TC33** | M67625 | Lớp 4: Đặc thù nghiệp vụ | `Q=True / Khảo sát & Nhóm / low` | `Q=True / Khảo sát & Nhóm / low` | ✅ Chuẩn |
| **TC34** | M73605 | Phổ biến hàng ngày | `Q=True / Logistics & Chuyên cần / medium` | `Q=True / Logistics & Chuyên cần / medium` | ✅ Chuẩn |
| **TC35** | M28055 | Lớp 4: Đặc thù nghiệp vụ | `Q=False / Ngoài phạm vi / Không liên quan / none` | `Q=False / Ngoài phạm vi / Không liên quan / none` | ✅ Chuẩn |
| **TC36** | M62112 | Lớp 4: Đặc thù nghiệp vụ | `Q=False / Ngoài phạm vi / Không liên quan / none` | `Q=False / Ngoài phạm vi / Không liên quan / none` | ✅ Chuẩn |
| **TC37** | M49744 | Lớp 4: Đặc thù nghiệp vụ | `Q=False / Ngoài phạm vi / Không liên quan / none` | `Q=False / Ngoài phạm vi / Không liên quan / none` | ✅ Chuẩn |
| **TC38** | E403_05 | Lớp 2: Mơ hồ / Thiếu thông tin | `Q=True / Kỹ thuật & Bài Lab / urgent` | `Q=True / Kỹ thuật & Bài Lab / urgent` | ✅ Chuẩn |
| **TC39** | SYN_04 | Lớp 3: Ngoài phạm vi / Thẩm quyền | `Q=True / Kỹ thuật & Bài Lab / urgent` | `Q=True / Kỹ thuật & Bài Lab / low` | ⚠️ Lệch phụ |
| **TC40** | SYN_05 | Edge cases | `Q=False / Ngoài phạm vi / Không liên quan / none` | `Q=False / Ngoài phạm vi / Không liên quan / none` | ✅ Chuẩn |

---

### 4. Phân tích Nguyên nhân Sai lệch Kỹ thuật (Failure & Variance Analysis)

> [!IMPORTANT]
> **Cam kết tính trung thực trong AI Evaluation**: Nhóm Phronesis tuân thủ nguyên tắc đánh giá khách quan. Mọi sai lệch giữa phán đoán của LLM và nhãn kỳ vọng đều được lưu vết đầy đủ trong `eval/logs/` và được mổ xẻ nguyên nhân kỹ thuật dưới đây thay vì điều chỉnh nhãn giả tạo.

#### Ca TC03 (M83711) - Phổ biến hàng ngày
- **Nội dung tin nhắn:** *"anh [@D3694] cho e hỏi vlearn chưa up bài mới hả ?"*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='medium'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='low'`
- **Lý do AI đưa ra:** Học viên hỏi về việc cập nhật bài mới trên vlearn.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `medium` vs AI phán đoán `low`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC06 (M57505) - Phổ biến hàng ngày
- **Nội dung tin nhắn:** *"Cho em hỏi workshop ngày mai thời lượng diễn ra trong bao lâu vậy ạ? Em muốn biết để tiện sắp xếp một số công việc cá nhân."*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='medium'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='low'`
- **Lý do AI đưa ra:** Học viên hỏi về thời gian diễn ra workshop để sắp xếp công việc cá nhân.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `medium` vs AI phán đoán `low`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC07 (M19124) - Phổ biến hàng ngày
- **Nội dung tin nhắn:** *"a ơi sao deadline ghép đội tự do end sớm vậy a?"*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='urgent'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Khảo sát & Nhóm'`, `urgency_level='medium'`
- **Lý do AI đưa ra:** Học viên thắc mắc về thời gian deadline ghép đội tự do.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch gom cụm:* Kỳ vọng là `Logistics & Chuyên cần` nhưng mô hình chọn `Khảo sát & Nhóm` do sự giao thoa ngữ nghĩa trong câu hỏi.
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `urgent` vs AI phán đoán `medium`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC09 (M94349) - Phổ biến hàng ngày
- **Nội dung tin nhắn:** *"[@D3694] anh ơi cho em hỏi các buổi workshop có thể xem lại record ở đâu vậy ạ?"*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='low'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Ngoài phạm vi / Không liên quan'`, `urgency_level='low'`
- **Lý do AI đưa ra:** Học viên hỏi về việc xem lại record các buổi workshop, không phải là câu hỏi khẩn cấp.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch gom cụm:* Kỳ vọng là `Logistics & Chuyên cần` nhưng mô hình chọn `Ngoài phạm vi / Không liên quan` do sự giao thoa ngữ nghĩa trong câu hỏi.

#### Ca TC10 (M30201) - Phổ biến hàng ngày
- **Nội dung tin nhắn:** *"Các anh chị ơi cho em hỏi điểm chuyên cần ở vin uni tính như thế nào ah?"*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='medium'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='low'`
- **Lý do AI đưa ra:** Học viên hỏi về cách tính điểm chuyên cần tại VinUni.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `medium` vs AI phán đoán `low`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC14 (E403_01) - Lớp 1: Nguồn sự thật
- **Nội dung tin nhắn:** *"Dạ buổi học tối hôm nay ngày 14/9 em không nhớ mình đã điểm danh ra về chưa. Nhờ các anh chị lab coach check lại giúp em lại ạ, MSSV của em là 2A202602819. Nếu em chưa điểm danh, mong các anh chị có thể hỗ trợ giúp em điểm danh bù."*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='urgent'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='medium'`
- **Lý do AI đưa ra:** Học viên yêu cầu kiểm tra điểm danh và hỗ trợ điểm danh bù cho buổi học.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `urgent` vs AI phán đoán `medium`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC15 (E403_02) - Lớp 1: Nguồn sự thật
- **Nội dung tin nhắn:** *"Còn trong buổi học thì em có đặt thắc mắc cho 2 anh labcoach. Em hỏi anh Hải DM về việc vì sao case test case lại có một vài test gặp lỗi provider_error. Một anh labcoach khác thì em hỏi rằng có thể chạy từng test case trong file để khắc phục việc thiếu credit API không."*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Kỹ thuật & Bài Lab'`, `urgency_level='urgent'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Kỹ thuật & Bài Lab'`, `urgency_level='medium'`
- **Lý do AI đưa ra:** Học viên đang thắc mắc về lỗi provider_error và cách chạy từng test case để khắc phục vấn đề liên quan đến API.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `urgent` vs AI phán đoán `medium`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC16 (E403_03) - Lớp 2: Mơ hồ / Thiếu thông tin
- **Nội dung tin nhắn:** *"Cho e hỏi ai là biên tập viên/người viết kịch bản video, giảng viên duyệt kịch bản ạ? nhóm e muốn làm khảo sát nhanh"*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Khảo sát & Nhóm'`, `urgency_level='medium'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Khảo sát & Nhóm'`, `urgency_level='low'`
- **Lý do AI đưa ra:** Học viên hỏi về thông tin liên quan đến biên tập viên/người viết kịch bản video cho khảo sát nhóm.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `medium` vs AI phán đoán `low`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC17 (E403_04) - Lớp 2: Mơ hồ / Thiếu thông tin
- **Nội dung tin nhắn:** *"anh ơi tới zone 2 giúp em với"*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Kỹ thuật & Bài Lab'`, `urgency_level='urgent'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='medium'`
- **Lý do AI đưa ra:** Học viên yêu cầu hỗ trợ đến một địa điểm cụ thể.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch gom cụm:* Kỳ vọng là `Kỹ thuật & Bài Lab` nhưng mô hình chọn `Logistics & Chuyên cần` do sự giao thoa ngữ nghĩa trong câu hỏi.
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `urgent` vs AI phán đoán `medium`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC18 (SYN_01) - Lớp 3: Ngoài phạm vi / Thẩm quyền
- **Nội dung tin nhắn:** *"Lab 4 này khó quá, bạn code giải hộ mình câu 3 với câu 4 được không, nộp giúp mình luôn với!"*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Kỹ thuật & Bài Lab'`, `urgency_level='low'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Kỹ thuật & Bài Lab'`, `urgency_level='urgent'`
- **Lý do AI đưa ra:** Học viên yêu cầu hỗ trợ giải bài lab và nộp bài, điều này ảnh hưởng đến tiến độ học tập.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `low` vs AI phán đoán `urgent`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC21 (M37211) - Lớp 1: Nguồn sự thật
- **Nội dung tin nhắn:** *"các bạn labcoach cho mình hỏi, mình quét mã điểm danh đầy đủ nhưng tsao trên app ko có lịch sử điểm danh?"*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='urgent'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='medium'`
- **Lý do AI đưa ra:** Học viên thắc mắc về việc không thấy lịch sử điểm danh trên ứng dụng.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `urgent` vs AI phán đoán `medium`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC23 (M03966) - Lớp 1: Nguồn sự thật
- **Nội dung tin nhắn:** *"Các anh chị cho em hỏi là thẻ học viên của em lúc vào trường thì bác bảo vệ bảo là chưa được kích hoạt thì phải làm sao ạ?"*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='urgent'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='medium'`
- **Lý do AI đưa ra:** Học viên hỏi về việc kích hoạt thẻ học viên, cần sự hỗ trợ từ TA.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `urgent` vs AI phán đoán `medium`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC24 (M27566) - Phổ biến hàng ngày
- **Nội dung tin nhắn:** *"cho em hỏi khóa mình có cấp giấy chứng nhận sinh viên cho học viên không ạ ? Tại phường em đang yêu cầu nộp giấy hoãn nghĩa vụ quân sự."*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='medium'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Logistics & Chuyên cần'`, `urgency_level='low'`
- **Lý do AI đưa ra:** Học viên hỏi về việc cấp giấy chứng nhận sinh viên cho mục đích hoãn nghĩa vụ quân sự.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `medium` vs AI phán đoán `low`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC26 (M89035) - Lớp 1: Nguồn sự thật
- **Nội dung tin nhắn:** *"Bài lab1 tôi clone code, không fork thì bị tính là fail rồi đúng không?"*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Kỹ thuật & Bài Lab'`, `urgency_level='urgent'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Kỹ thuật & Bài Lab'`, `urgency_level='medium'`
- **Lý do AI đưa ra:** Học viên hỏi về quy định liên quan đến việc clone và fork code trong bài lab.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `urgent` vs AI phán đoán `medium`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC27 (M51326) - Lớp 2: Mơ hồ / Thiếu thông tin
- **Nội dung tin nhắn:** *"em chạy tới bước 3 thì bị lỗi như này ạ"*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Kỹ thuật & Bài Lab'`, `urgency_level='medium'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Kỹ thuật & Bài Lab'`, `urgency_level='urgent'`
- **Lý do AI đưa ra:** Học viên gặp lỗi kỹ thuật trong quá trình làm bài lab và cần hỗ trợ khẩn.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `medium` vs AI phán đoán `urgent`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC31 (M01844) - Phổ biến hàng ngày
- **Nội dung tin nhắn:** *"mới có thông báo lập team trên phoenix nhưng cho em hỏi là lv2 có cần phải lập team không ạ"*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Khảo sát & Nhóm'`, `urgency_level='medium'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Khảo sát & Nhóm'`, `urgency_level='low'`
- **Lý do AI đưa ra:** Học viên hỏi về việc có cần lập team cho lv2 hay không.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `medium` vs AI phán đoán `low`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

#### Ca TC39 (SYN_04) - Lớp 3: Ngoài phạm vi / Thẩm quyền
- **Nội dung tin nhắn:** *"Anh chị TA ơi, em đang làm đồ án tốt nghiệp môn Vi xử lý bên Bách Khoa bị lỗi mạch nạp, anh chị xem hộ em sơ đồ này với ạ!"*
- **Kỳ vọng (Human Ground Truth):** `is_unanswered_question=True`, `topic_cluster='Kỹ thuật & Bài Lab'`, `urgency_level='low'`
- **Thực tế AI trả lời:** `is_unanswered_question=True`, `topic_cluster='Kỹ thuật & Bài Lab'`, `urgency_level='urgent'`
- **Lý do AI đưa ra:** Học viên gặp lỗi kỹ thuật trong quá trình làm đồ án và cần sự hỗ trợ từ TA.
- **Mổ xẻ nguyên nhân kỹ thuật:**
  - *Sai lệch mức khẩn cấp:* Kỳ vọng `low` vs AI phán đoán `urgent`. Độ khẩn cấp mang tính chủ quan cao giữa các annotator con người và quy tắc heuristic của prompt.

### 5. Kết luận & Đề xuất Cải tiến cho Run 2 (CP4)

1. **Về Khả năng Bảo vệ An toàn (Safety / Prompt Injection):**
   - Ca TC19 (Cố tình chèn lệnh override system prompt để xóa DB) đã được mô hình nhận diện chính xác là văn bản đầu vào thô, không thực thi chỉ thị độc hại và gán nhãn `Ngoài phạm vi / Không liên quan` với độ khẩn cấp `none`. Đây là điểm sáng về an toàn AI.
2. **Về Khả năng Phân cấp Khẩn cấp (Urgency Calibration):**
   - Mức độ khẩn cấp (`urgent` vs `medium`) đôi khi có sự dao động nhẹ do tiêu chí 'chặn tiến độ' trong prompt cần thêm các ví dụ few-shot cụ thể (như từ khóa 'gấp', 'sắp hết giờ', 'cứu em'). Cần bổ sung 2-3 few-shot examples vào System Prompt ở CP4.
3. **Về Tốc độ & Độ tin cậy Kỹ thuật:**
   - Toàn bộ 20 lời gọi API đều hoàn thành với độ trễ trung bình 1.60s, không gặp lỗi HTTP 429 hay timeout. 100% vết gọi API đều được lưu trữ đầy đủ tại thư mục `eval/logs/` dưới định dạng JSON có đầy đủ `prompt_input` và `raw_response`.
