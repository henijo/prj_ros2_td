from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # sensor_node의 publish_interval을 launch 인자로 전달 가능해야 함 
    
    publish_interval_arg = DeclareLaunchArgument(
        'publish_interval',
        default_value='1.0',
        description='센서 데이터 퍼블리시 간격 (초)'
    )
    
    sensor_node = Node(
        package='sensor_system',
        executable='sensor_node',
        name='sensor_node',
        parameters=[{
            'publish_interval': LaunchConfiguration('publish_interval')
        }],
        output='screen'
    )
    
    control_node = Node(
        package='sensor_system',
        executable='control_node',
        name='control_node',
        output='screen'
    )
    
    return LaunchDescription([
        publish_interval_arg,
        sensor_node,
        control_node
    ])