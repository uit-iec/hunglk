# 📄 Hướng dẫn cập nhật nội dung website

Trang web này sử dụng các file YAML để quản lý và hiển thị nội dung như tin tức, bài báo, và hoạt động học thuật. Dưới đây là cách bạn có thể cập nhật nội dung trong các file `news.yaml`, `research.yaml`, và `activities.yaml`.

---

## 📢 1. Tin tức & cập nhật mới nhất tại `_data/news.yaml`

### ➕ Cách thêm một tin mới:
Mỗi mục trong `news.yaml` cần có định dạng như sau:

```yaml
- date: 2025-03
  title: Tên sự kiện hoặc công bố
  venue: (tùy chọn) Tên hội nghị hoặc nơi diễn ra
  type: (tùy chọn) Loại hoạt động, ví dụ: Research Paper, Talk, Award
  award: (tùy chọn) Giải thưởng (nếu có)
  locations: (tùy chọn) - Danh sách địa điểm/đơn vị
  links:
    - pdf: https://example.com/paper.pdf
    - code: https://github.com/example/repo
```

✅ Ghi chú:
- date nên dùng định dạng YYYY-MM để dễ sắp xếp.

- links là danh sách, có thể bao gồm pdf, code, video, v.v.

- Các mục sẽ được tự động sắp xếp theo thời gian (mới nhất hiển thị trước).

## 📚 2. Cập nhập danh sách công bố khoa học tại `_data/research.yaml`
Gồm 2 phần:
- categorys: Danh sách các lĩnh vực (ví dụ: Security, NLP, IoT)
- research: Danh sách bài báo kèm theo thông tin

🧩 Ví dụ:
```yaml
categorys:
  - name: iot
    title: Internet of Things
  - name: security
    title: Security & Privacy

research:
  - title: Tên bài báo
    authors: A. Tác giả, B. Người khác
    year: 2024
    publication: SIGMOD
    category: security
```
✅ Ghi chú:
- category phải khớp với name trong categorys.
- Bài viết sẽ được nhóm theo category và sắp xếp theo year (mới nhất trước).

## 🧑‍🏫 3. Cập nhập các hoạt động chuyên môn tại `_data/activities.yaml`
```yaml
- role: PC Member
  event: VLDB 2024
- role: Associate Editor
  event: TKDE Journal
- role: Invited Talk
  event: Google Research
```
✅ Ghi chú:
- Hoạt động sẽ hiển thị theo danh sách, không cần thời gian cụ thể.
- Bạn có thể phân loại hoạt động nếu muốn mở rộng.


## 🔧 Hướng Dẫn Cấu Hình Website với _config.yml (Jekyll)
File config.yml là nơi chứa tất cả các thiết lập chính cho website của bạn. Việc chỉnh sửa đúng cách sẽ giúp hiển thị thông tin cá nhân, bài viết và chức năng của trang hiệu quả hơn.

1. 🏷 Thiết lập cơ bản
```yaml
title: "Kim-Hung Le"             # Tiêu đề chính của website
description: "personal description"  # Mô tả ngắn về bạn hoặc website (phục vụ SEO)
url: https://ntruongn.github.io  # Địa chỉ trang chính (GitHub Pages hoặc custom domain)
baseurl: "jekyll-academic-cv"    # Thư mục con (nếu dùng GitHub Pages)
```
2. 👤 Thông tin cá nhân (Hiển thị bên thanh trái)
```yaml
author:
  name: "Kim-Hung Le"
  location: "Room 8.4, Building E, UIT - VNUHCM"
  email: "hunglk@uit.edu.vn"
  github: "hunglkuit"
  googlescholar: "https://scholar.google.com/..."
  avatar       : "avatar.jpg"  # Image file stored in /images/
  bio          : "Lecturer at University of Information Technology (VNUHCM-UIT), specialized in IoT and computer networks."
  description  : > 
    Lecturer at University of Information Technology (VNUHCM-UIT), specialized in IoT and computer networks."
```
📌 Bạn có thể cập nhật các đường link mạng xã hội hoặc email tại đây.

3. 📚 Danh mục bài viết (Publications)
Dùng để phân loại bài viết nghiên cứu của bạn:
```yaml
publication_category:
  books:
    title: 'Books'
  manuscripts:
    title: 'Journal Articles'
  conferences:
    title: 'Conference Papers'
```
📝 Những key như books, manuscripts,... sẽ được dùng trong file research.yaml.

4. ⚙️ Các thiết lập hiển thị
```yaml
locale: "en-US"
read_more: "disabled"      # Bật/Tắt nút "Đọc thêm"
breadcrumbs: false         # Bật/Tắt breadcrumbs (đường dẫn trên cùng trang)
```

5. 🧩 Plugin và tính năng
Các plugin đã tích hợp sẵn:
  ```yaml
  plugins:
    - jekyll-feed
    - jekyll-sitemap
    - jekyll-paginate
  ```
  🔌 Bạn chỉ cần chỉnh khi muốn thêm tính năng mới (ít khi cần thay đổi).
6. 📈 Thiết lập theo dõi (Analytics) và SEO
Nếu bạn có dùng Google Analytics:
```yaml
analytics:
  provider: "google-analytics-4"
  google:
    tracking_id: "G-XXXXXXX"
```
7. 🌍 Cấu hình triển khai
```yaml
repository: "yourusername/your-repo-name"
timezone: Etc/UTC
```
Nếu triển khai trên GitHub Pages, hãy cập nhật đúng tên repo tại đây.