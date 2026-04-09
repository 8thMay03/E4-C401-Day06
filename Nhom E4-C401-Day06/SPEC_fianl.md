# SPEC - AI Product Hackathon

**Nhóm:** E4_C401
**Track:** ☐ VinFast · ☐ Vinmec · ☐ VinUni-VinSchool · ☑ XanhSM · ☐ Open
**Problem statement (1 câu):** *Tài xế XanhSM hiện gặp khó khăn hỏi đáp vấn đề về chính sách, thu nhập thông qua chatbot*

---

## 1. AI Product Canvas

|   | Value | Trust | Feasibility |
|---|-------|-------|-------------|
| **Câu hỏi** | User nào? Pain gì? AI giải gì? | Khi AI sai thì sao? User sửa bằng cách nào? | Cost/latency bao nhiêu? Risk chính? |
| **Trả lời** | Tài xế XanhSM mất thời gian chờ support, AI trả lời tức thì (chính sách, thu nhập), giảm chờ từ vài giờ xuống <3s | AI sai => tài xế click "Report error" => feedback => admin verify => KB update => model retrain weekly | ~$0.001-0.01/truy vấn, latency <3s, risk: hallucinate chính sách/địa điểm cần verification layer & KB sync |

**Automation hay augmentation?** ☐ Automation · ☑ Augmentation
Justify: *Augmentation - tài xế thấy gợi ý từ AI, có thể click "Liên hệ support" nếu không hài lòng, cơ chế feedback giúp model cải thiện liên tục*

**Learning signal:**

1. User correction đi vào đâu? => Feedback button => correction logs => admin review => update knowledge base => retrain model weekly
2. Product thu signal gì để biết tốt lên hay tệ đi? => Thumbs up/down ratio, "report error" count, escalation-to-support rate, response latency, user satisfaction survey
3. Data thuộc loại nào? ☐ User-specific · ☑ Domain-specific · ☑ Real-time · ☑ Human-judgment · ☐ Khác:...
   Có marginal value không? Có - domain-specific data từ XanhSM (chính sách, bảng giá, địa điểm, TOS) hiếm/không có sẵn trong pre-trained models

---

## 2. User Stories - 4 paths

### Feature 1: Trả lời câu hỏi chính sách & thu nhập

**Trigger:** *Tài xế mở chatbot => nhập câu hỏi về chính sách (VD: "Cách tính tiền commit") => AI trả lời => ...*

| Path | Câu hỏi thiết kế | Mô tả |
|------|-------------------|-------|
| Happy - AI đúng, tự tin | Tài xế thấy gì? Flow kết thúc ra sao? | *AI trả lời rõ ràng với confidence 90%, hiển thị source, tài xế click like, tiếp tục làm việc* |
| Low-confidence - AI không chắc | System báo "không chắc" bằng cách nào? Tài xế quyết thế nào? | *AI trả lời nhưng hiển thị confidence 65%, đồng thời hiện nút "Liên hệ support ngay", tài xế có thể escalate* |
| Failure - AI sai | Tài xế biết AI sai bằng cách nào? Recover ra sao? | *AI trả lời sai về commission, tài xế click "Report error", submit feedback, hệ thống ghi nhận, admin review trong 24h* |
| Correction - tài xế báo cáo | Tài xế báo cáo bằng cách nào? Data đó đi vào đâu? | *Click "Report error" => mô tả vấn đề => submit => correction log => admin verify + update KB => retrain* |


Rule_cost : quy tắc để tính thu nhập.

Cách tính tiền quốc xe như sau:
-Đối với xanh Sm bike 
"tổng quãng đường ( kilomet )" x 6000VNĐ - "(5% thuế )"  = "tổng số tiền"
=> tổng số tiền tài xế nhận được là bằng 30% "tổng số tiền "
-Đối với xanh Sm car 
"tổng quãng đường ( kilomet )" x 11000VNĐ - "(5% thuế )"  = "tổng số tiền"
=> tổng số tiền tài xế nhận được là bằng 35% "tổng số tiền "
Tổng thu nhập trong 1 ngày bằng " tổng số tiền " của tất cả quốc xe đã chạy trong hôm nay đối với cả xanh sm car và xanh sm bike 

Nếu giờ hoạt động trong khung giờ cao điểm đối với một cuốc xe chạy xong ( đã ra được tổng số tiền)
các cuốc xe đó sẽ được cộng thêm  "điểm thưởng".
- Đối với xanh sm bike 
+ Khung giờ được chia như sau:

6 giờ đến 8 giờ 59 phút : cộng thêm 10 điểm thưởng với xanh sm bike 
11 giờ đến 13 giờ 59 phút : cộng 5 điểm thưởng
16 giờ tới 18 giờ 59 phút : cộng 10 điểm thưởng 
các khung giờ còn lại sẽ là: 5 điểm thưởng

- Đối với xanh sm car :
6 giờ đến 8 giờ 59 phút : cộng thêm 10 điểm thưởng với xanh sm bike 
11 giờ đến 13 giờ 59 phút : cộng 5 điểm thưởng
16 giờ tới 18 giờ 59 phút : cộng 10 điểm thưởng 
các khung giờ còn lại sẽ là: 5 điểm thưởng

đối với 100 điểm trên 1 ngày sẽ được 10000 VNĐ
đối với 200 điểm trên 1 ngày sẽ được 40000 VNĐ
đối với 300 điểm trên 1 ngày sẽ được 80000 VNĐ
Dịch vụ Xanh SM bike

### Feature 2: Tìm trạm sạc & nơi sửa xe gần nhất

**Trigger:** *Tài xế gõ "Trạm sạc gần đây nhất" hoặc "Sửa xe ở đâu" => AI trả lời với location => ...*

| Path | Câu hỏi thiết kế | Mô tả |
|------|-------------------|-------|
| Happy - AI đúng, tự tin | Tài xế thấy gì? Flow kết thúc ra sao? | *AI trả lời với địa chỉ, bản đồ, giờ mở cửa, tài xế click "Điều hướng" => được đưa vào Maps* |
| Low-confidence - AI không chắc | System báo "không chắc" bằng cách nào? Tài xế quyết thế nào? | *AI hiển thị 3 địa điểm, tài xế chọn 1 hoặc gõ filter (VD: "buổi tối")* |
| Failure - AI sai | Tài xế biết AI sai bằng cách nào? Recover ra sao? | *AI gợi ý trạm sạc đóng cửa rồi, tài xế phát hiện khi tới => click "Thông tin cũ" => feedback* |
| Correction - tài xế báo cáo | Tài xế báo cáo bằng cách nào? Data vào đâu? | *Click "Thông tin không chính xác" => select loại lỗi (đóng cửa, sai giờ) => submit => KB update* |

---

## 3. Eval metrics + threshold

**Optimize precision hay recall?** ☐ Precision · ☑ Recall
Tại sao? *Recall cao => AI trả lời được nhiều câu hỏi tài xế => tác xế ít phải escalate => giảm chi phí support, tăng user satisfaction*
Nếu sai ngược lại thì chuyện gì xảy ra? *Nếu low recall (precision cao) => AI chỉ trả lời câu chắc chắn, bỏ sót nhiều câu => tài xế phải escalate liên tục => phải chờ support => bỏ dùng*

| Metric | Threshold | Red flag (dừng khi) |
|--------|-----------|---------------------|
| Recall (% câu hỏi được trả lời) | ≥80% | <70% trong 1 tuần liên tục |
| Thumbs-up/down ratio | ≥75% | <60% trong 3 ngày (có sai nhưng trả lời được thì ok) |
| Escalation-to-support rate | ≤15% | >25% (AI bỏ sót quá nhiều) |
| Avg response latency | second | >5 second (UX deteriorate) |

---

## 4. Top 3 failure modes

| # | Trigger | Hậu quả | Mitigation |
|---|---------|---------|------------|
| 1 | AI trả lời thông tin chính sách CŨ (đã thay đổi) với confidence cao | Tài xế quyết định hành động dựa trên info sai => không lợi nhuận, rủi ro pháp lý | Đồng bộ cơ sở tri thức (KB) hằng ngày khi có cập nhật chính sách, áp dụng cơ chế kiểm soát độ tin cậy (confidence-gating), và kiểm tra thủ công các câu trả lời liên quan đến chính sách theo tuần. |
| 2 | AI hallucinate địa điểm trạm sạc/sửa xe (không tồn tại hoặc sai) | Tài xế lái xe tới, lãng phí xăng/thời gian, thất vọng => churn | Chỉ cung cấp các địa điểm đã được xác thực từ cơ sở dữ liệu đối tác theo thời gian thực, không sử dụng AI để tự sinh dữ liệu; áp dụng lớp kiểm tra và xác thực nghiêm ngặt trước khi trả kết quả. |
| 3 | Volume cao => AI latency chậm (>5s) => tài xế chờ lâu => abandon | Tài xế chuyển sang support/competitor => ROI âm | Mở rộng (scale)GPU, triển khai cơ chế cache cho 100 câu hỏi & trả lời phổ biến nhất, và chuyển sang phản hồi FAQ tĩnh nếu độ trễ vượt quá ngưỡng cho phép. |

---

## 5. ROI 3 kịch bản

|   | Conservative | Realistic | Optimistic |
|---|-------------|-----------|------------|
| **Assumption** |500 tài xế/ngày, 60% hài lòng, policy đơn giản | 2000 tài xế/ngày, 80% hài lòng | 5000 tài xế/ngày, 90% hài lòng, strong flywheel |
| **Cost** | $20/ngày inference + $10 KB update | $80/ngày inference + $30 KB | $150/ngày inference + $50 KB |
| **Benefit** | Reduce support 4h/day × $15/h = $60/day, +2% retention | Reduce support 15h/day = $225/day, +5% retention | Reduce support 30h/day = $450/day, +10% retention |
| **Net** | $60 - $30 = $30/day | $225 - $110 = $115/day | $450 - $200 = $250/day |

**Kill criteria:** *Net benefit <0 trong 2 tháng liên tục, hoặc precision <70%, hoặc user churn >5%*

---

## 6. Mini AI spec

**Product overview:** XanhSM Support AI là chatbot augmentation hỗ trợ tài xế XanhSM giải đáp nhanh về chính sách, thu nhập, trạm sạc, sửa xe. Thay vì chờ support, tài xế nhận câu trả lời <3s hoặc escalate nếu AI không chắc.

**User & Pain:** Tài xế XanhSM mất thời gian chờ support, không thể quyết định nhanh => giảm hiệu suất kiếm tiền, app bị chỉ trích.

**AI Role:** Augmentation - AI trả lời tức thì, tài xế feedback ngay nếu sai hoặc escalate to human, không phải 100% automation => giảm risk, tăng trust.

**Quality:** Precision ≥85% (ưu tiên) - tài xế phải tin, nếu sai ảnh hưởng kiếm tiền. Latency <3s, thumbs-up ≥80%.

**Top Risks:**
1. **Hallucination policy/location** => mitigation: real-time KB sync, only serve verified data
2. **Knowledge stale** => policy thay đổi AI trả lời cũ => mitigation: daily KB update, flag & audit
3. **Scale bottleneck** => 5000+ users latency => mitigation: GPU scaling, cache, fallback FAQ

**Data Flywheel:** Driver question => AI answer => Feedback => Admin verify => KB update => Retrain weekly => Better quality => Higher adoption => More signals => Improve loop.

**Success Metrics:** ROI $115/day (realistic), precision 80%+, adoption >50% active drivers.
