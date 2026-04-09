# Prototype - Trợ lý tài xế XanhSM

## Mô tả dự án
Trợ lý tài xế XanhSM giúp giải đáp các thắc mắc của tài xế xung quanh chính sách, thu nhập. Tài xế đưa câu hỏi lên hệ thống, hệ thống đưa ra câu trả lời phù hợp với chính sách của XanhSM.

## Level: Mock prototype
- UI build bằng Streamlit
- 1 flow chính chạy thật với OpenAI API: nhập câu hỏi liên quan đến chính sách => Trả lời dựa vào chính sách của XanhSM (đã được upload trên hệ thống)

## Links
- Prompt test log: xem file `app.py`
- Slide demo: 

## Tools
- UI: Streamlit
- AI: OpenAI GPT 4o
- Prompt: system prompt 'config.py'

## Phân công
| Thành viên | Phần | Output |
|-----------|------|--------|
| Lưu Thị Ngọc Quỳnh | Canvas, failure modes, dữ liệu | Slide, SPEC.md, Quy tắc bảo vệ quyền lợi người tiêu dùng.txt |
| Lưu Quang Lực | Lọc data, crawl dữ liệu | khach_hang.txt, Chính sách bảo vệ dữ liệu cá nhân.txt |
| Đinh Văn Thư | User Case, trải nghiệm người dùng, crawl dữ liệu | ĐIỀU KHOẢN CHUNG HỢP ĐỒNG DỊCH VỤ.txt, user-flow-promt.md |
| Nguyễn Phương Nam | System promt, work flow | config.py, spec/eval-metrics.md |
| Nguyễn Bá Khánh|Nạp dữ liệu cho Agent|ingest.py, document_loader.py|
| Lý Quốc An| Build giao diện|App.py, chain.py, vector_store.py|
|Nguyễn Quốc Khánh| Tạo logic cho chatbot, lọc dữ liệu|app.py, embeddings.py, retriever.py, text_splitter.py |
|Nguyễn Quang Minh| Test case | prompt-test-log.md, test.py|