import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from xuwenyu_homework1_interfaces.msg import HomeworkData


class HomeworkSubscriber(Node):
    def __init__(self):
        super().__init__('XuwenyuSubscriber')
        self.subscription = self.create_subscription(
            HomeworkData,
            '/XuwenyuTopic',
            self.receive_message,
            10
        )

    def receive_message(self, msg):
        self.get_logger().info(
            f'Received: {msg.text}, {msg.number}, {msg.decimal_value}'
        )


def main():
    rclpy.init()
    node = HomeworkSubscriber()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
