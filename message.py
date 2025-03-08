from linebot.models import FlexSendMessage

def create_product_bubble_msg():
    flex_contents = [
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://example.com/product1.jpg",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {"type": "text", "text": "商品 1", "weight": "bold", "size": "xl"},
                    {"type": "text", "text": "$1000", "color": "#888888", "size": "sm"}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "postback",
                            "label": "下單",
                            "data": "order=商品1&price=1000"
                        }
                    }
                ]
            }
        },
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://example.com/product2.jpg",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {"type": "text", "text": "商品 2", "weight": "bold", "size": "xl"},
                    {"type": "text", "text": "$1500", "color": "#888888", "size": "sm"}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "postback",
                            "label": "下單",
                            "data": "order=商品2&price=1500"
                        }
                    }
                ]
            }
        }
    ]

    return FlexSendMessage(
        alt_text="商品資訊",
        contents={"type":"carousel", "contents":flex_contents}
    )