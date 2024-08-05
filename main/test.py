from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# Existing app logic here


@app.route('/', methods=['GET', 'POST'])
def handle_keepalive():
    print(request)
    if request.method == 'POST':
        # Handle image upload here
        if 'image' in request.files:
            file = request.files['image']
            if file.filename != '':
                media_path = './'  # Adjust as necessary
                filename = os.path.join(media_path, file.filename)
                file.save(filename)
                return "Image successfully uploaded", 200
        return "No image uploaded", 400
    else:
        # Respond to GET request, potentially for keepalive
        return "Connection alive", 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=52345)  # Adjust port as necessary
