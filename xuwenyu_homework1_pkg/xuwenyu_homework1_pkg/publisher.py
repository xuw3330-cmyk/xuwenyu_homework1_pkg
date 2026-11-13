import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from xuwenyu_homework1_interfaces.msg import HomeworkData


class HomeworkPublisher(Node):
    def __init__(self):
        super().__init__('XuwenyuPublisher')
        self.publisher = self.create_publisher(HomeworkData, '/XuwenyuTopic', 10)
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        msg = HomeworkData()
        msg.text = 'xuwenyu'
        msg.number = 12
        msg.decimal_value = 1.01
        self.publisher.publish(msg)
        self.get_logger().info(
            f'Sent: {msg.text}, {msg.number}, {msg.decimal_value}'
        )


def main():
    rclpy.init()
    node = HomeworkPublisher()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
