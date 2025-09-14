# 📸 Insta-Unfollowers  

A **Python tool** to get Instagram follower insights — find out who doesn’t follow you back, and who you don’t follow back.  

---

## 🚀 Features  
- ✅ Export a list of users you are **following**  
- ✅ Export a list of users who are **following you**  
- ✅ Find **users who don’t follow you back**  
- ✅ Find **users you don’t follow back**  

All results are saved into clean, easy-to-read text files.  

---

## 📂 Output Files  
1. `followees.txt` → Users you are following  
2. `followers.txt` → Users who are following you  
3. `unfollowers.txt` → Users you follow but they don’t follow back  
4. `not_following_back.txt` → Users who follow you but you don’t follow back  

---

## ⚙️ Prerequisites  
1. Install the [**Cookie-Editor Chrome Extension**](https://chromewebstore.google.com/detail/ookdjilphngeeeghgngjabigmpepanpl?utm_source=item-share-cb)  
2. Log in to Instagram → Export cookies via the extension (⚠️ No password included) click on extension -> cookies editor -> opens a tab -> export cookies.
3. Save cookies as `cookies.json`  
4. Edit **line 74 and 75** in `insta_unfollowers.py` with your **Instagram username** and path to your `cookies.json`  

---

## 🛠️ Installation & Usage  

### 1. Clone the repository  
```bash
git clone https://github.com/your-username/Insta-Unfollowers.git
cd Insta-Unfollowers
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the script
```bash
python insta_unfollowers.py
```