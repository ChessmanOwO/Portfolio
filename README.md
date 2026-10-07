# Portfolio - Nguyễn Hà Phong

Portfolio tĩnh dùng HTML, Tailwind CSS CDN và các tài nguyên trong `assets/`.

## Chạy kèm form liên hệ (Flask)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
py server.py
```

Mở `http://localhost:8085`. Dữ liệu form được lưu cục bộ trong `portfolio.db`.

GitHub Pages chỉ phục vụ nội dung tĩnh, không chạy `server.py`; vì vậy form liên hệ cần được nối với một backend được host riêng nếu triển khai bằng Pages.
