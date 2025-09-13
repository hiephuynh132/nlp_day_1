from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Danh sách 10 keyword và câu trả lời tương ứng
KEYWORDS_RESPONSES = {
    "menu": "Chúng tôi có cafe sữa, cafe đen, trà sữa và bánh ngọt.",
    "giờ mở cửa": "Quán mở cửa từ 7h sáng đến 10h tối.",
    "địa chỉ": "Quán chúng tôi ở 123 Đường ABC, Quận 1, TP.HCM.",
    "giá": "Giá đồ uống từ 30k đến 70k.",
    "wifi": "Quán có wifi miễn phí, mật khẩu là cafe123.",
    "đặt bàn": "Bạn có thể đặt bàn trước qua số điện thoại 0123456789.",
    "khuyến mãi": "Hiện tại quán có giảm giá 10% cho khách hàng thân thiết.",
    "bánh": "Chúng tôi có bánh mì, bánh ngọt và bánh ngọc trai.",
    "ship": "Chúng tôi có dịch vụ giao hàng qua Grab và Gojek.",
    "feedback": "Chúng tôi luôn mong nhận được góp ý từ khách hàng!"
}

def get_response(message):
    """Tìm keyword trong message và trả về câu trả lời tương ứng"""
    message_lower = message.lower()
    for keyword, response in KEYWORDS_RESPONSES.items():
        if keyword in message_lower:
            return response
    return "Xin lỗi, tôi không hiểu. Bạn có thể hỏi điều khác về quán cafe không?"


@app.route("/")
def index():
    # render index.html trong thư mục templates/
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chatbot():
    data = request.json
    if "message" not in data:
        return jsonify({"error": "Missing 'message' field"}), 400
    
    user_message = data["message"]
    bot_response = get_response(user_message)
    
    return jsonify({
        "user_message": user_message,
        "bot_response": bot_response
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
