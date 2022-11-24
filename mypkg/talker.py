import rclpy
from rclpy.node import Node
from person_msg.srv import Query

def cb(request, response):
    if request.name == "伊藤雪":
        response.age = 19
    else:
        response.age = 255

    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)
