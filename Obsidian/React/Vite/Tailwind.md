## 1. Install
1. 
```cmd
npm create vite@latest ./ -- --template react
```
2. 
```cmd
npm install -D tailwindcss postcss autoprefixer

npx tailwindcss init -p
```
3. 
- set path
```tailwind.config.js
content: ["./index.html", "./src/**/*.{js, ts, jsx, tsx}"]
```
4. 
- add to css 
```index.css
@tailwind base;
@tailwind components;
@tailwind utilities;
```
