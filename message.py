def create_product_bubble_msg(products):
    flex_contents = []
    for i in range(len(products)):
        content = {
            "type":"bubble",
            "hero":{
                "type":"image",
                "url":products[i]['images'][0],
                "size":"full",
                "aspectRatio":"20:13",
                "aspectMode":"cover"
            },
            "body":{
                "type":"box",
                "layout":"vertical",
                "contnets":[
                    {"type": "text", "text": products[i]['name'], "weight": "bold", "size": "xl"},
                    {"type": "text", "text": products[i]['price'], "color": "#888888", "size": "sm"}
                ]
            },
            "footer":{
                "type":"box",
                "layout":"vertical",
                "contents":[
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "postback",
                            "label": "下單",
                            "data": f"order={products[i]['name']}&price={products[i]['price']}"
                        }
                    }
                ]
            }
        }
        flex_contents.append(content)
    
    return flex_contents