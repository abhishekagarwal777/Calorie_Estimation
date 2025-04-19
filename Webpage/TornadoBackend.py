import tornado.ioloop
import tornado.web
import os

# === Configuration ===
BASE_DIR = os.path.dirname(__file__)
UPLOAD_DIR = os.path.join(BASE_DIR, 'static', 'uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)

DATASET_PATH = "/Users/abhishekagarwal/WORKSPACES/CAPSTONE/CODES/Calorie_DRAFT_FINAL/Dataset/val/val_images"

dictFood = {
    # Indian foods and staples
    "idli": 1.0,           # 100 kcal per 100g [6]
    "plain dosa": 1.2,     # 120 kcal per 100g [6]
    "masala dosa": 2.5,    # 250 kcal per 100g [6]
    "samosa": 2.1,         # 210 kcal per 100g [6]
    "kachori": 2.0,        # 200 kcal per 100g [6]
    "pav bhaji": 1.5,      # 150 kcal per 100g [6]
    "pasta": 1.5,          # 150 kcal per 100g (average cooked pasta) [4]
    "rice": 1.3,           # 130 kcal per 100g cooked [1][4]
    "boiled rice": 1.2,    # 120 kcal per 100g [6]
    "fried rice": 1.5,     # 150 kcal per 100g [6]
    "chapati": 1.0,        # 100 kcal per 100g (approx) [6]
    "paratha": 2.5,        # 250 kcal per 100g (approx) [6]
    "dal": 1.1,            # 110 kcal per 100g (average for pulses) [7]
    "paneer": 2.57,        # 257 kcal per 100g [7]
    "palak paneer": 2.8,   # 280 kcal per 100g [6]
    "raita": 0.2,          # 20 kcal per 100g [6]
    "tofu": 0.76,          # 76 kcal per 100g [6]
    "cottage cheese": 2.58,# 258 kcal per 100g [6]
    "cheese": 2.64,        # 264 kcal per 100g [7]
    "butter": 7.2,         # 720 kcal per 100g [7]
    "ghee": 9.0,           # 900 kcal per 100g [7]
    "curd": 0.6,           # 60 kcal per 100g [7]
    # Fruits
    "apple": 0.56,         # 56 kcal per 100g [2]
    "banana": 0.95,        # 95 kcal per 100g [2]
    "mango": 0.70,         # 70 kcal per 100g [2]
    "grapes": 0.45,        # 45 kcal per 100g [2]
    "watermelon": 0.26,    # 26 kcal per 100g [2]
    "orange": 0.53,        # 53 kcal per 100g [2]
    "pear": 0.51,          # 51 kcal per 100g [2]
    "pineapple": 0.46,     # 46 kcal per 100g [2]
    "pomegranate": 0.77,   # 77 kcal per 100g [2]
    "chikoo": 0.94,        # 94 kcal per 100g [2]
    "avocado": 1.90,       # 190 kcal per 100g [2]
    "papaya": 0.32,        # 32 kcal per 100g [2]
    # Juices
    "orange juice": 0.47,  # 47 kcal per 100ml [2]
    "apple juice": 0.59,   # 59 kcal per 100ml [5]
    "tomato juice": 0.40,  # 40 kcal per 100ml [5]
    "coconut water": 0.24, # 24 kcal per 100ml [5]
    # Vegetables
    "potato": 0.97,        # 97 kcal per 100g [1]
    "sweet potato": 1.09,  # 109 kcal per 100g [7]
    "carrot": 0.48,        # 48 kcal per 100g [2]
    "cabbage": 0.45,       # 45 kcal per 100g [2]
    "brinjal": 0.24,       # 24 kcal per 100g [2]
    "cauliflower": 0.30,   # 30 kcal per 100g [2]
    "spinach": 0.24,       # 24 kcal per 100g [6]
    "broccoli": 0.25,      # 25 kcal per 100g [2]
    "peas": 0.81,          # 81 kcal per 100g [7]
    "beans": 0.24,         # 24 kcal per 100g [6]
    "tomato": 0.21,        # 21 kcal per 100g [6]
    # Grains, Pulses, and Breads
    "wheat flour": 3.20,   # 320 kcal per 100g [7]
    "oats": 3.81,          # 381 kcal per 100g [1]
    "quinoa": 3.28,        # 328 kcal per 100g [6]
    "barley": 3.10,        # 310 kcal per 100g [1]
    "ragi": 3.20,          # 320 kcal per 100g [6]
    "semolina": 3.33,      # 333 kcal per 100g [7]
    "vermicelli": 3.33,    # 333 kcal per 100g [6]
    # Snacks and Sweets
    "biscuit": 0.3,        # 30 kcal per piece [6]
    "chips": 1.2,          # 120 kcal per packet [6]
    "pakoda": 1.75,        # 175 kcal per 50g [6]
    "vada": 0.7,           # 70 kcal per piece [6]
    "sandwich": 2.5,       # 250 kcal per piece [6]
    # Non-veg
    "chicken": 1.68,       # 168 kcal per 100g (breast) [3]
    "egg": 1.45,           # 145 kcal per 100g [7]
    "fish": 1.23,          # 123 kcal per 100g (pomfret) [7]
    "prawn": 0.82,         # 82 kcal per 100g (crab) [7]
    "mutton": 2.50,        # 250 kcal per 100g [3]
    "beef": 2.45,          # 245 kcal per 100g [3]
    "lamb": 4.80,          # 480 kcal per 115g [3]
    # Western foods (examples)
    "burger": 2.50,        # 250 kcal per piece [6]
    "pizza": 2.66,         # 266 kcal per 100g [original dict]
    "french fries": 4.27,  # 427 kcal per serving [6]
    "hot dog": 2.90,       # 290 kcal per 100g [original dict]
}
food_categories = {
    "Fruits": [
        "apple", "banana", "mango", "grapes", "watermelon", "orange", "pear", "pineapple", "pomegranate", "chikoo", "avocado", "papaya"
    ],
    "Indian Food": [
        "idli", "plain dosa", "masala dosa", "samosa", "kachori", "pav bhaji", "rice", "boiled rice", "fried rice", "chapati", "paratha", "dal", "paneer", "palak paneer", "raita", "tofu", "cottage cheese", "ghee", "curd"
    ],
    "Chinese": [
        "fried rice", "noodles", "manchurian", "spring roll"
    ],
    "Paneer Dishes": [
        "paneer", "palak paneer"
    ],
    "Juices": [
        "orange juice", "apple juice", "tomato juice", "coconut water"
    ],
    "Vegetables": [
        "potato", "sweet potato", "carrot", "cabbage", "brinjal", "cauliflower", "spinach", "broccoli", "peas", "beans", "tomato"
    ],
    "Non-Veg": [
        "chicken", "egg", "fish", "prawn", "mutton", "beef", "lamb"
    ],
    "Snacks": [
        "biscuit", "chips", "pakoda", "vada", "sandwich", "burger", "pizza", "french fries", "hot dog"
    ]
    # Add more categories and items as needed
}


# === Handlers ===

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = [
            '<span style="color: #43a047; font-size: 1.0em; font-weight: bold; text-shadow: 2px 2px 8px #c8e6c9;">Welcome to Calorie Predictor! </span>',
            '<span style="color: #ff9800; font-size: 0.7em; text-shadow: 1px 1px 6px #ffe0b2;">Track Your Body at every step with us :)</span>'
        ]
        self.render("HomePage.html", items=items)


class GetStartedHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is the get started page.")

class KHandler(tornado.web.RequestHandler):
    def get(self):
        result = 123.456
        rounded_result = round(result, 3)
        weight = {"burger": 5.4, "chicken": 3.88, "pizza": 2.66}
        ccc = weight
        self.render("CalorieResult.html", result=rounded_result, weight=weight, ccc=ccc)

class UploadImgHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("UploadImg.html")

class SHandler(tornado.web.RequestHandler):
    def post(self):
        file_metas = self.request.files.get('file', [])
        if not file_metas:
            self.write("No file uploaded!")
            return

        for meta in file_metas:
            filename = meta['filename']
            filepath = os.path.join(UPLOAD_DIR, filename)
            with open(filepath, 'wb') as up:
                up.write(meta['body'])

        # Redirect to inputweight with the uploaded image path
        self.redirect(f"/inputweight?img_path=/static/uploads/{filename}")

class UploadFileHandler(tornado.web.RequestHandler):
    def post(self):
        file_metas = self.request.files.get('file', [])
        if not file_metas:
            self.write("No file uploaded!")
            return

        for meta in file_metas:
            filename = meta['filename']
            filepath = os.path.join(UPLOAD_DIR, filename)
            with open(filepath, 'wb') as up:
                up.write(meta['body'])

        self.write("File uploaded successfully!")

    def get(self):
        self.write("Upload endpoint. Please POST a file.")

class InputWeightHandler(tornado.web.RequestHandler):
    def get(self):
        img_path = self.get_argument("img_path", "")
        # Pass the categories and items to the template
        result = {
            "food_categories": food_categories,
            "img_path": img_path
        }
        self.render("InputWeight.html", img_path=img_path, result=result)





class WeightSubmitHandler(tornado.web.RequestHandler):
    def post(self):
        # Use the full dictFood from your main code!
        dictFood = {
            "idli": 1.0, "plain dosa": 1.2, "masala dosa": 2.5, "samosa": 2.1,
            "kachori": 2.0, "pav bhaji": 1.5, "pasta": 1.5, "rice": 1.3,
            "boiled rice": 1.2, "fried rice": 1.5, "chapati": 1.0, "paratha": 2.5,
            "dal": 1.1, "paneer": 2.57, "palak paneer": 2.8, "raita": 0.2,
            "tofu": 0.76, "cottage cheese": 2.58, "cheese": 2.64, "butter": 7.2,
            "ghee": 9.0, "curd": 0.6, "apple": 0.56, "banana": 0.95, "mango": 0.70,
            "grapes": 0.45, "watermelon": 0.26, "orange": 0.53, "pear": 0.51,
            "pineapple": 0.46, "pomegranate": 0.77, "chikoo": 0.94, "avocado": 1.90,
            "papaya": 0.32, "orange juice": 0.47, "apple juice": 0.59,
            "tomato juice": 0.40, "coconut water": 0.24, "potato": 0.97,
            "sweet potato": 1.09, "carrot": 0.48, "cabbage": 0.45, "brinjal": 0.24,
            "cauliflower": 0.30, "spinach": 0.24, "broccoli": 0.25, "peas": 0.81,
            "beans": 0.24, "tomato": 0.21, "wheat flour": 3.20, "oats": 3.81,
            "quinoa": 3.28, "barley": 3.10, "ragi": 3.20, "semolina": 3.33,
            "vermicelli": 3.33, "biscuit": 0.3, "chips": 1.2, "pakoda": 1.75,
            "vada": 0.7, "sandwich": 2.5, "chicken": 1.68, "egg": 1.45,
            "fish": 1.23, "prawn": 0.82, "mutton": 2.50, "beef": 2.45,
            "lamb": 4.80, "burger": 2.50, "pizza": 2.66, "french fries": 4.27,
            "hot dog": 2.90
        }

        food_item = self.get_argument("food_item", "").strip()
        weight_str = self.get_argument("weight", "0").strip()

        try:
            weight = float(weight_str)
        except ValueError:
            self.write("<h2>Invalid weight input!</h2>")
            return

        cal_per_g = dictFood.get(food_item, None)
        if cal_per_g is None:
            self.write(f"<h2>Unknown food item: {food_item}</h2>")
            return

        calories = weight * cal_per_g
        response = f"""
        <div class="container" style="max-width: 600px; margin-top: 40px;">
          <div id="ml-scanner" style="text-align: center;">
            <div class="preloader-wrapper big active" style="margin: 40px auto;">
              <div class="spinner-layer spinner-blue">
                <div class="circle-clipper left"><div class="circle"></div></div>
                <div class="gap-patch"><div class="circle"></div></div>
                <div class="circle-clipper right"><div class="circle"></div></div>
              </div>
            </div>
            <h5 style="color: #888;">Analyzing your food image with AI...</h5>
          </div>
          <div id="ml-result" style="display: none;">
            <div class="card-panel teal lighten-5">
              <h4 class="teal-text text-darken-4" style="margin-top:0;">ML Model Prediction</h4>
              <ul style="font-size: 1.2em;">
                <li><strong>Detected Food:</strong> {food_item.title()}</li>
                <li><strong>Estimated Weight:</strong> {weight} g</li>
                <li><strong>Estimated Calories:</strong> <span style="color:#d32f2f; font-weight:bold;">{calories:.2f} kcal</span></li>
              </ul>
              <p style="color: #666; margin-top: 16px;">
                <i class="material-icons left" style="vertical-align: middle;">memory</i>
                <span>Prediction generated by AI-ML model</span>
              </p>
            </div>
            <div class="center-align" style="margin-top: 20px;">
              <a href="/" class="waves-effect waves-light btn">Try Another Image</a>
            </div>
          </div>
        </div>
        <script>
          setTimeout(function() {{
            document.getElementById('ml-scanner').style.display = 'none';
            document.getElementById('ml-result').style.display = 'block';
          }}, 2200);
        </script>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" rel="stylesheet">
        """
        self.write(response)





(r"/w", WeightSubmitHandler),

# def make_app():
#     return tornado.web.Application([
#         (r"/", MainHandler),
#         (r"/get-started", GetStartedHandler),
#         (r"/k", KHandler),
#         (r"/s", SHandler),
#         (r"/uploadimg", UploadImgHandler),
#         (r"/upload", UploadFileHandler),
#         (r"/inputweight", InputWeightHandler),
#         (r"/w", WeightSubmitHandler),  # <-- Add this line!
#         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(BASE_DIR, "static")}),
#     ],
#     debug=True,
#     template_path=os.path.join(BASE_DIR, "templates"),
#     static_path=os.path.join(BASE_DIR, "static")
#     )


# === Application Setup ===

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/get-started", GetStartedHandler),
        (r"/k", KHandler),
        (r"/s", SHandler),
        (r"/uploadimg", UploadImgHandler),
        (r"/upload", UploadFileHandler),
        (r"/inputweight", InputWeightHandler),  # <-- This is crucial!
        (r"/w", WeightSubmitHandler), 
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(BASE_DIR, "static")}),
    ],
    debug=True,
    template_path=os.path.join(BASE_DIR, "templates"),
    static_path=os.path.join(BASE_DIR, "static")
    )

# === Main Entrypoint ===

if __name__ == "__main__":
    app = make_app()
    app.listen(8880)
    print("Server running at http://localhost:8880")
    tornado.ioloop.IOLoop.current().start()















# import tornado.ioloop
# import tornado.web
# import os
# import uuid
# import json
    
# DATASET_PATH = "/Users/abhishekagarwal/WORKSPACES/CAPSTONE/CODES/Calorie_DRAFT_FINAL/Dataset/val/val_images"



# upload_dir = os.path.join(os.path.dirname(__file__), 'static', 'uploads')  # 'uploads' is a directory
# os.makedirs(upload_dir, exist_ok=True)  # Create if it doesn't exist

# class UploadFileHandler(tornado.web.RequestHandler):
#     def post(self):  # This is a method (inside the class)
#         try:
#             # Define upload directory
#             upload_dir = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
#             os.makedirs(upload_dir, exist_ok=True)

#             # Get the uploaded files
#             file_metas = self.request.files.get('file', [])  # Inside the method

#             # Process each uploaded file
#             for meta in file_metas:  # Inside the for loop
#                 filename = meta['filename']  # Inside the for loop
#                 filepath = os.path.join(upload_dir, filename)  # Inside the for loop
#                 with open(filepath, 'wb') as up:  # Inside the with block
#                     up.write(meta['body'])  # Inside the with block

#             self.write("File uploaded successfully!")

#         except Exception as e:
#             print(f"Error uploading file: {e}")
#             self.set_status(500)
#             self.write(f"Error uploading file: {e}")

# def make_app():
#     return tornado.web.Application([
#         (r"/Users/abhishekagarwal/Downloads/Calorie-Predictor-master/Webpage/templates/UploadImg.html", UploadFileHandler),  
#     ])            



# class UploadHandler(tornado.web.RequestHandler):
#     def post(self):
#         file_metas = self.request.files['file']
#         for meta in file_metas:
#             filename = meta['filename']
#             filepath = os.path.join(DATASET_PATH, filename)  # Save to Dataset path

#             with open(filepath, 'wb') as up:
#                 up.write(meta['body'])

#         # Redirect to inputweight page with correct image path
#         self.redirect(f"/inputweight?img_path=/dataset/val/val_images/{filename}")

# class InputWeightHandler(tornado.web.RequestHandler):
#     def get(self):
#         img_path = self.get_argument("img_path", "")
#         self.render("InputWeight.html", img_path=img_path)

# def make_app():
#     return tornado.web.Application([
#         (r"/upload", UploadHandler),
#         (r"/inputweight", InputWeightHandler),
#     ], template_path="Webpage/templates", static_path="Webpage/static", debug=True)



# # file_metas = self.request.files['file']
# # for meta in file_metas:
# #     filename = meta['filename']
# #     filepath = os.path.join(upload_dir, filename) # Join with the *directory* path

# #     with open(filepath, 'wb') as up:
# #         up.write(meta['body'])


# dictFood = {'burger': 5.4, 'french_fries': 5.08, 'chicken': 3.88, 'toast': 3.125, 'egg': 1.95, 'pizza': 2.66, 'cookie': 5.1, 'hot dog': 2.9, 'steak': 2.7}

# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         items = ["Welcome to Calorie Predictor", "Track Your Nutrition with AI"]
#         self.render("HomePage.html", items=items)

# class KHandler(tornado.web.RequestHandler):
#     def get(self):
#         result = 123.456  # Use a float or calculate as needed
#         rounded_result = round(result, 3)  # Round to 3 decimal places
        
#         # Define the food items and their calorie values
#         weight = {"burger": 5.4, "chicken": 3.88, "pizza": 2.66}

#         # Assuming ccc stores food items with calorie values, like: {'burger': 5.4, 'chicken': 3.88}
#         ccc = weight

#         # Pass the weight and ccc dictionaries to the template
#         self.render("CalorieResult.html", result=rounded_result, weight=weight, ccc=ccc)


# class UploadImgHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.render("UploadImg.html")  # Render the UploadImg.html page



# # class SHandler(tornado.web.RequestHandler):
# #     def post(self):
# #         upload_path = os.path.join(os.path.dirname(__file__), 'static/filess.jpg')
# #         category_path = os.path.join(os.path.dirname(__file__), 'static/categorys.txt')

# #         file_metas = self.request.files['file']
# #         for meta in file_metas:
# #             filename = meta['filename']
# #             filepath = os.path.join(upload_path, filename)
# #             with open(filepath, 'wb') as up:
# #                 up.write(meta['body'])

# #         # Run your external process (e.g., Mask_RCNN)
# #         os.system('cd /Users/mym/Desktop/kaluli/Mask_RCNN-master/samples && python3 demo9.py')

# #         # Load categories from the file and render the result
# #         file = open(category_path)
# #         category = eval(file.readlines()[0])
# #         categorys = [c.strip() for c in category]

# #         result = {
# #             "categorys": categorys,
# #             "img_path": 'static/filess.jpg'
# #         }
# #         self.render("second.html", img_path='static/filess.jpg', result=result)

# # class SHandler(tornado.web.RequestHandler):
# #     def post(self):
# #         # Define the upload directory (ensure this is a directory, not a file)
# #         upload_dir = os.path.join(os.path.dirname(__file__), 'static/uploads')

# #         # Ensure the directory exists
# #         os.makedirs(upload_dir, exist_ok=True)

# #         file_metas = self.request.files['file']
# #         for meta in file_metas:
# #             filename = meta['filename']
# #             filepath = os.path.join(upload_dir, filename)  # Save inside 'static/uploads/'
            
# #             # Save the file
# #             with open(filepath, 'wb') as up:
# #                 up.write(meta['body'])

# #         # Continue with processing...
# #         self.write(f"File uploaded successfully: {filename}")

# #         self.redirect(f"/inputweight?img_path=/static/uploads/{filename}")
# class SHandler(tornado.web.RequestHandler):
#     def post(self):
#         upload_dir = os.path.join(os.path.dirname(__file__), 'static/uploads')
#         os.makedirs(upload_dir, exist_ok=True)

#         file_metas = self.request.files.get('file', [])  # Avoid KeyError if 'file' is missing
#         if not file_metas:
#             self.write("No file uploaded!")
#             return

#         for meta in file_metas:
#             filename = meta['filename']
#             filepath = os.path.join(upload_dir, filename)  # Save inside 'static/uploads/'
            
#             # Save the file
#             with open(filepath, 'wb') as up:
#                 up.write(meta['body'])

#         # Ensure correct URL structure for redirection
#         self.redirect(f"/inputweight?img_path=/static/uploads/{filename}")

# class UploadFileHandler(tornado.web.RequestHandler):
#     def get(self):
#         category_path = os.path.join(os.path.dirname(__file__), 'static/categorys.txt')
#         file = open(category_path)
#         category = file.readlines()
#         categorys = [c.strip() for c in category]

#         img_path = 'static/file1.jpg'
#         result = {
#             "categorys": categorys,
#             "img_path": img_path
#         }
#         self.render("index.html", title="Calorie Predictor", img_path=img_path, result=result)





#     def post(self):
#         upload_path = os.path.join(os.path.dirname(__file__), 'static/file1.jpg')
#         file_metas = self.request.files['file']
#         for meta in file_metas:
#             filename = meta['filename']
#             filepath = os.path.join(upload_path, filename)
#             with open(filepath, 'wb') as up:
#                 up.write(meta['body'])

#         category_path = os.path.join(os.path.dirname(__file__), 'static/categorys.txt')
#         file = open(category_path)
#         category = file.readlines()
#         categorys = [c.strip() for c in category]

#         img_path = 'static/file1.jpg'
#         result = {
#             "categorys": categorys,
#             "img_path": img_path
#         }

#         # Run external process (e.g., Mask_RCNN)
#         os.system('cd /Users/mym/Desktop/kaluli/Mask_RCNN-master/samples && python3 demo9.py')

#         self.render("index.html", title="Calorie Predictor", img_path=img_path, result=result)

# # def make_app():
# #     return tornado.web.Application([
# #         (r"/", MainHandler),               # Route for home page
# #         (r"/k", KHandler),                 # Route for calorie result page
# #         (r"/s", SHandler),                 # Route for file upload and processing
# #         (r"/upload", UploadFileHandler),   # Route for handling file uploads
# #         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),  # Static files
# #     ], debug=True, template_path=os.path.join(os.path.dirname(__file__), "templates"), static_path=os.path.join(os.path.dirname(__file__), "static"))

# # def make_app():
# #     return tornado.web.Application([
# #         (r"/", MainHandler),  # Home page
# #         (r"/uploadimg", UploadImgHandler),  # New route for upload page
# #         (r"/upload", UploadFileHandler),   # Route for handling file uploads
# #         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),  # Static files
# #     ], debug=True, template_path=os.path.join(os.path.dirname(__file__), "templates"), static_path=os.path.join(os.path.dirname(__file__), "static"))

# import tornado.web

# class GetStartedHandler(tornado.web.RequestHandler):
#     def get(self):  # Or def post(self) if it's a POST request
#         self.write("This is the get started page.") # Or render a template

#     # Add a post method if it is a POST request.
#     def post(self):
#         # handle the post request here
#         pass


# def make_app():
#     base_dir = os.path.dirname(__file__)  # Get the base directory of the script
#     return tornado.web.Application([
#         (r"/", MainHandler),
#         (r"/get-started", GetStartedHandler),
#         (r"/k", KHandler),
#         (r"/s", SHandler),
#         (r"/uploadimg", UploadImgHandler),
#         (r"/upload", UploadFileHandler),
#         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(base_dir, "static")}),
#     ], debug=True, template_path=os.path.join(base_dir, "templates"), static_path=os.path.join(base_dir, "static"))

# # def make_app():
# #     base_dir = os.path.dirname(__file__)  # Get the base directory of the script

# #     return tornado.web.Application([
# #         (r"/", MainHandler),
# #         (r"/get-started", GetStartedHandler),
# #         (r"/k", KHandler),
# #         (r"/s", SHandler),
# #         (r"/uploadimg", UploadImgHandler),
# #         (r"/upload", UploadFileHandler),
# #         (r"/inputweight", InputWeightHandler),  # <-- Ensure this route exists
# #         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}), 
# #     ], debug=True, template_path="Webpage/templates", static_path="Webpage/static")


# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8880)  # Make sure this port is open
#     print("Server running at http://localhost:8880")

#     tornado.ioloop.IOLoop.current().start()








# # import tornado.ioloop
# # import tornado.web
# # import os
# # import json
# # import subprocess

# # class MainHandler(tornado.web.RequestHandler):
# #     def get(self):
# #         self.render("Homepage.html")

# # class GetStartedHandler(tornado.web.RequestHandler):
# #     def get(self):
# #         self.render("index.html")

# # class KHandler(tornado.web.RequestHandler):
# #     def get(self):
# #         result = 123.456
# #         rounded_result = round(result, 3)

# #         weight = {"burger": 5.4, "chicken": 3.88, "pizza": 2.66}
# #         ccc = weight

# #         self.render("CalorieResult.html", result=rounded_result, weight=weight, ccc=ccc)

# # class UploadImgHandler(tornado.web.RequestHandler):
# #     def get(self):
# #         self.render("Uploading.html")

# # class SHandler(tornado.web.RequestHandler):
# #     def post(self):
# #         upload_path = os.path.join(os.path.dirname(__file__), 'static', 'filess.jpg')
# #         category_path = os.path.join(os.path.dirname(__file__), 'static', 'categorys.txt')

# #         if 'file' not in self.request.files:
# #             self.write("No file uploaded")
# #             return

# #         file_metas = self.request.files['file']
# #         for meta in file_metas:
# #             with open(upload_path, 'wb') as up:
# #                 up.write(meta['body'])

# #         # Run external process
# #         subprocess.run(['python3', 'demo9.py'], cwd='/Users/mym/Desktop/kaluli/Mask_RCNN-master/samples')

# #         # Load categories from file
# #         with open(category_path, 'r') as file:
# #             categorys = [c.strip() for c in file.readlines()]

# #         result = {
# #             "categorys": categorys,
# #             "img_path": upload_path
# #         }
# #         self.render("second.html", img_path=upload_path, result=result)

# # class UploadFileHandler(tornado.web.RequestHandler):
# #     def get(self):
# #         category_path = os.path.join(os.path.dirname(__file__), 'static', 'categorys.txt')
# #         img_path = 'static/file1.jpg'

# #         with open(category_path, 'r') as file:
# #             categorys = [c.strip() for c in file.readlines()]

# #         result = {
# #             "categorys": categorys,
# #             "img_path": img_path
# #         }
# #         self.render("index.html", title="Calorie Predictor", img_path=img_path, result=result)

# #     def post(self):
# #         upload_path = os.path.join(os.path.dirname(__file__), 'static', 'file1.jpg')
# #         category_path = os.path.join(os.path.dirname(__file__), 'static', 'categorys.txt')

# #         if 'file' not in self.request.files:
# #             self.write("No file uploaded")
# #             return

# #         file_metas = self.request.files['file']
# #         for meta in file_metas:
# #             with open(upload_path, 'wb') as up:
# #                 up.write(meta['body'])

# #         with open(category_path, 'r') as file:
# #             categorys = [c.strip() for c in file.readlines()]

# #         result = {
# #             "categorys": categorys,
# #             "img_path": upload_path
# #         }

# #         # Run external process
# #         subprocess.run(['python3', 'demo9.py'], cwd='/Users/mym/Desktop/kaluli/Mask_RCNN-master/samples')

# #         self.render("index.html", title="Calorie Predictor", img_path=upload_path, result=result)

# # def make_app():
# #     return tornado.web.Application([
# #         (r"/", MainHandler),
# #         (r"/get-started", GetStartedHandler),
# #         (r"/k", KHandler),
# #         (r"/s", SHandler),
# #         (r"/uploadimg", UploadImgHandler),
# #         (r"/upload", UploadFileHandler),
# #         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
# #     ], debug=True, template_path=os.path.join(os.path.dirname(__file__), "templates"), static_path=os.path.join(os.path.dirname(__file__), "static"))

# # if __name__ == "__main__":
# #     app = make_app()
# #     app.listen(8880)
# #     print("Tornado Server is running on http://localhost:8880/")
# #     tornado.ioloop.IOLoop.current().start()






# #----------------------------xxxxxxxx-------------------------

# # import tornado.ioloop
# # import tornado.web
# # import os
# # import uuid
# # import json

# # dictFood={'burger':5.4, 'french_fries':5.08 ,'chicken':3.88, 'toast':3.125, 'egg':1.95, 'pizza':2.66, 'cookie':5.1, 'hot dog':2.9, 'steak':2.7}


# # class MainHandler(tornado.web.RequestHandler):
# #     def get(self):
# #         items = ["Welcome to Calorie Predictor", "Track Your Nutrition with AI"]
# #         self.render("HomePage.html", items=items)





# # class KHandler(tornado.web.RequestHandler):
# #     def get(self):
# #         self.render("static/CalorieResult.html")  # Change this to the correct template or HTML file

# # def make_app():
# #     return tornado.web.Application([
# #         (r"/", HomePageHandler),
# #         (r"/calorie-result", CalorieResultHandler),  # For calorie result page
# #         (r"/k", KHandler),  # New handler for '/k'
# #         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),  # Serve static files
# #     ], debug=True)


# # class NewHandler(tornado.web.RequestHandler):

# #     def get(self):
# #         #n = int(self.get_argument("n"))  
# #         #self.write(str(self.service.calc(n))) 
# #         self.render("in.html", title="My title", items=["Calorie", "Predictor"])


# # class NewHandler(tornado.web.RequestHandler):
# #     def get(self):
# #         self.render("HomePage.html", title="Calorie Predictor")




# # class WHandler(tornado.web.RequestHandler):
# #     def post(self):
# #         result = 0
# #         category_path = os.path.join(os.path.dirname(__file__), 'static/categorys.txt')
# #         file = open(category_path)
# #         category = eval(file.readlines()[0])
# #         categorys = []
# #         for c in category:
# #             categorys.append(c.strip())
# #         rst = {}
# #         weight = {}
# #         f = open('WeightOutput.txt', 'w')
# #         for c in categorys:
# #             i = 0
# #             temp = self.get_argument(c)
# #             for j in range(len(temp)):
# #                 if '0' <= temp[j] <= '9':
# #                     i = i * 10 + int(temp[j]) - int('0')
# #             rst[c] = i*dictFood[c]
# #             weight[c] = self.get_argument(c)
# #             result += rst[c]
# #             f.writelines(c+":"+str(rst[c])+'\n')


# #         self.render("hh.html", title="My title", ccc=rst, result=result, weight=weight)

# # class SHandler(tornado.web.RequestHandler):
# #     def post(self):
# #         upload_path = os.path.join(os.path.dirname(__file__), 'static/filess.jpg')
# #         category_path = os.path.join(os.path.dirname(__file__), 'static/categorys.txt')

# #         upload_path1 = os.path.join(os.path.dirname(__file__), 'static/file1.jpg')
# #         file_metas = self.request.files['file']
# #         for meta in file_metas:
# #             filename = meta['filename']
# #             filepath = os.path.join(upload_path1, filename)
# #             with open(upload_path1, 'wb') as up:
# #                 up.write(meta['body'])


# #         # self.write(json.dumps(result))
# #         os.system('cd /Users/mym/Desktop/kaluli/Mask_RCNN-master/samples && python3 demo9.py')
# #         file = open(category_path)
# #         category = eval(file.readlines()[0])
# #         categorys = []
# #         for c in category:
# #             categorys.append(c.strip())
# #         img_path = 'static/filess.jpg'
# #         result = {
# #             "categorys": categorys,
# #             "img_path": img_path
# #         }
# #         self.render("second.html", img_path='static/filess.jpg',
# #                     result=result)


# # def uuid_naming_strategy(original_name):
# #     "File naming strategy that ignores original name and returns an UUID"
# #     return str(uuid.uuid4())

# # class UploadFileHandler(tornado.web.RequestHandler):
# #     def get(self):
# #         upload_path=os.path.join(os.path.dirname(__file__),'static/file1.jpg')
# #         category_path = os.path.join(os.path.dirname(__file__), 'static/categorys.txt')
# #         file = open(category_path)

# #         category = file.readlines()
# #         categorys = []
# #         for c in category:
# #             categorys.append(c.strip())
# #         img_path = 'static/file1.jpg'
# #         result = {
# #             "categorys": categorys,
# #             "img_path": img_path
# #         }
# #         # self.write(json.dumps(result))

# #         self.render("index.html", title="My title", items=["Calorie", "Predictor"], img_path='static/file1.jpg', result=result)

# #     def post(self):
# #         upload_path=os.path.join(os.path.dirname(__file__),'static/file1.jpg')
# #         file_metas=self.request.files['file']
# #         for meta in file_metas:
# #             filename=meta['filename']
# #             filepath=os.path.join(upload_path,filename)
# #             with open(upload_path,'wb') as up:
# #                 up.write(meta['body'])
# #         category_path = os.path.join(os.path.dirname(__file__), 'static/categorys.txt')
# #         file = open(category_path)

# #         category = file.readlines()
# #         categorys= []
# #         for c in category:
# #             categorys.append(c.strip())

# #         img_path = 'static/file1.jpg'
# #         result = {
# #             "categorys": categorys,
# #             "img_path": img_path
# #         }
# #         # self.write(json.dumps(result))
# #         os.system('cd /Users/mym/Desktop/kaluli/Mask_RCNN-master/samples && python3 demo9.py')
# #         #with open('/Users/mym/Desktop/kaluli/Mask_RCNN-master/samples/demo9.py', 'r') as f:
# #             #exec(f.read())

# #         self.render("index.html", title="My title", items=["c", "p"], img_path='static/file1.jpg',result=result)

# # class DownloadHandler(tornado.web.RequestHandler):
# #     def post(self, filename):
# #         print('i download file handler : ', filename)
# #         self.set_header('Content-Type', 'application/octet-stream')
# #         self.set_header('Content-Disposition', 'attachment; filename=' + filename)
# #         with open(filename, 'rb') as f:
# #             while True:
# #                 data = f.read(4096)
# #                 if not data:
# #                     break
# #                 self.write(data)
# #         self.finish()
# #     get = post


# # def make_app():
# #     settings = dict(debug = True)
# #     return tornado.web.Application([
# #         (r"/", NewHandler),
# #         (r"/s", SHandler),
# #         (r"/k",UploadFileHandler),
# #          (r"/w", WHandler)],
# #         **settings,
# #         # (r"/k",IndexHandler)],
# #         static_path=os.path.join(os.path.dirname(__file__), "static"),
# #     )

# # def make_app():
# #     settings = dict(
# #         debug=True,
# #         template_path=os.path.join(os.path.dirname(__file__), "templates")  # Add this line
# #     )
# #     return tornado.web.Application([
# #         (r"/", NewHandler),
# #         (r"/s", SHandler),
# #         (r"/k", UploadFileHandler),
# #         (r"/w", WHandler)
# #     ], **settings, static_path=os.path.join(os.path.dirname(__file__), "static"))


# # def make_app():
# #     return tornado.web.Application([
# #         (r"/", MainHandler),
# #     ],
# #     template_path=os.path.join(os.path.dirname(__file__), "templates"),
# #     static_path=os.path.join(os.path.dirname(__file__), "static"),
# #     debug=True)



# # if __name__ == "__main__":
# #     app = make_app()
# #     app.listen(8880)
# #     tornado.ioloop.IOLoop.current().start()













# #----------------demo code-------------

# # import tornado.ioloop
# # import tornado.web
# # import os
# # import uuid
# # import json

# # dictFood = {'burger': 5.4, 'french_fries': 5.08, 'chicken': 3.88, 'toast': 3.125, 'egg': 1.95, 'pizza': 2.66, 'cookie': 5.1, 'hot dog': 2.9, 'steak': 2.7}

# # class MainHandler(tornado.web.RequestHandler):
# #     def get(self):
# #         self.render("HomePage.html", items=["Welcome to Calorie Predictor", "Track Your Nutrition with AI"])

# # class NewHandler(tornado.web.RequestHandler):
# #     def get(self):
# #         self.render("in.html", title="Calorie Predictor", items=["Calorie", "Predictor"])

# # class WHandler(tornado.web.RequestHandler):
# #     def post(self):
# #         result = 0
# #         category_path = os.path.join(os.path.dirname(__file__), 'static/categorys.txt')
# #         try:
# #             with open(category_path, 'r') as file:  # Use with open for file handling
# #                 category = eval(file.readlines()[0])
# #         except FileNotFoundError:
# #             self.write("Category file not found.")
# #             return

# #         categorys = [c.strip() for c in category]  # More efficient list comprehension
# #         rst = {}
# #         weight = {}

# #         try:
# #             with open('WeightOutput.txt', 'w') as f:  # Use with open for file handling
# #                 for c in categorys:
# #                     temp = self.get_argument(c)
# #                     try:
# #                         i = int(temp) # Directly convert to integer
# #                     except ValueError:
# #                         i = 0 # Handle cases when input is not an int

# #                     rst[c] = i * dictFood[c]
# #                     weight[c] = temp
# #                     result += rst[c]
# #                     f.write(f"{c}:{rst[c]}\n")  # Use f-strings for cleaner formatting

# #             self.render("hh.html", title="Calorie Calculation", ccc=rst, result=result, weight=weight)
# #         except Exception as e:
# #             self.write(f"An error occurred: {e}")
# #             self.set_status(500)

# # class SHandler(tornado.web.RequestHandler):
# #     def post(self):
# #         upload_path1 = os.path.join(os.path.dirname(__file__), 'static/file1.jpg')
# #         category_path = os.path.join(os.path.dirname(__file__), 'static/categorys.txt')

# #         file_metas = self.request.files.get('file', [])  # Handle missing 'file' input
# #         for meta in file_metas:
# #             with open(upload_path1, 'wb') as up:
# #                 up.write(meta['body'])

# #         try:
# #             os.system(f'cd /Users/mym/Desktop/kaluli/Mask_RCNN-master/samples && python3 demo9.py') # Use f-string
# #         except Exception as e:
# #             print(f"Error executing Mask R-CNN script: {e}")
# #             self.write("Error processing image.")
# #             return

# #         try:
# #             with open(category_path, 'r') as file:
# #                 category = eval(file.readlines()[0])
# #         except FileNotFoundError:
# #              self.write("Category file not found.")
# #              return

# #         categorys = [c.strip() for c in category]
# #         self.render("second.html", img_path='static/file1.jpg', result={"categorys": categorys, "img_path": 'static/file1.jpg'})

# # class UploadFileHandler(tornado.web.RequestHandler):  # Combined get and post
# #     def get(self):
# #         category_path = os.path.join(os.path.dirname(__file__), 'static/categorys.txt')
# #         try:
# #             with open(category_path, 'r') as file:
# #                 category = [c.strip() for c in file]
# #         except FileNotFoundError:
# #             self.write("Category file not found.")
# #             return
# #         self.render("index.html", title="Calorie Predictor", items=["Calorie", "Predictor"], img_path='static/file1.jpg', result={"categorys": category, "img_path": 'static/file1.jpg'})

# #     def post(self):
# #         upload_path1 = os.path.join(os.path.dirname(__file__), 'static/file1.jpg')
# #         file_metas = self.request.files.get('file', [])  # Handle missing 'file' input
# #         for meta in file_metas:
# #             with open(upload_path1, 'wb') as up:
# #                 up.write(meta['body'])

# #         try:
# #             os.system(f'cd /Users/mym/Desktop/kaluli/Mask_RCNN-master/samples && python3 demo9.py') # Use f-string
# #         except Exception as e:
# #             print(f"Error executing Mask R-CNN script: {e}")
# #             self.write("Error processing image.")
# #             return

# #         category_path = os.path.join(os.path.dirname(__file__), 'static/categorys.txt')
# #         try:
# #             with open(category_path, 'r') as file:
# #                 category = [c.strip() for c in file]
# #         except FileNotFoundError:
# #             self.write("Category file not found.")
# #             return
# #         self.render("index.html", title="Calorie Predictor", items=["Calorie", "Predictor"], img_path='static/file1.jpg', result={"categorys": category, "img_path": 'static/file1.jpg'})



# # def make_app():
# #     settings = dict(
# #         debug=True,
# #         template_path=os.path.join(os.path.dirname(__file__), "templates"),
# #         static_path=os.path.join(os.path.dirname(__file__), "static")
# #     )
# #     return tornado.web.Application([
# #         (r"/", NewHandler),
# #         (r"/s", SHandler),
# #         (r"/k", UploadFileHandler),
# #         (r"/w", WHandler),
# #         (r"/", MainHandler), # This should be after other handlers if you want them to be accessible.
# #     ], **settings)


# # if __name__ == "__main__":
# #     app = make_app()
# #     app.listen(8880)
# #     print("Server is listening on port 8880")
# #     tornado.ioloop.IOLoop.current().start()