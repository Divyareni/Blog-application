# 📝 Blog Application

A full-stack blog platform allowing users to create, edit, publish, and browse blog posts. Designed to be easy to run and modify — ideal for personal blogs or as a starter project for blogging functionality.


---

## ✅ Features

- User authentication (Register/Login/Logout)
- Create, update, and delete blog posts
- View all published blogs
- View individual blog post details
- (Optional) Commenting, tags, and media upload
- Responsive UI
- Containerized setup via Docker

---

## 🚀 Getting Started

### Prerequisites

Ensure the following are installed:

- Node.js (v14+ recommended)
- npm or yarn
- MongoDB or other database (if required)
- Git

---

### 🔧 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/Divyareni/Blog-application.git
cd Blog-application

2. Install Backend Dependencies
cd backend
npm install

3. (Optional) Install Frontend Dependencies

cd ../frontend
npm install

4. Configure Environment Variables

Create a .env file in the backend/ directory:

PORT=3000
DATABASE_URL=mongodb://localhost:27017/blogdb
JWT_SECRET=yourSecretKey

**Running the App**

Start Backend:

cd backend
npm run dev    # or npm start


(Optional) Start Frontend:

cd ../frontend
npm start


Visit: http://localhost:3000

🧪 **API Endpoints** (Example)
Method	Endpoint	Description
POST	/api/auth/register	Register new user
POST	/api/auth/login	Login & receive token
GET	/api/posts	Get all posts
POST	/api/posts	Create new post
GET	/api/posts/:id	Get single post
PUT	/api/posts/:id	Update a post
DELETE	/api/posts/:id	Delete a post


🛠️ **Environment Variables**

Create a .env file with:

PORT=3000
DATABASE_URL=mongodb://localhost:27017/blogdb
JWT_SECRET=yourSecretKey
NODE_ENV=development


If using cloud services:

CLOUDINARY_CLOUD_NAME=your_cloud
CLOUDINARY_API_KEY=your_key
CLOUDINARY_API_SECRET=your_secret

📋 **Usage**

Register or login

Create a new blog post

Edit/delete your own posts

View others' posts

(Optional) Add comments or likes (if implemented)



