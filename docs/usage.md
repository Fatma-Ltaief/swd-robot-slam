```markdown
# Usage

## Launch robot description

```bash
ros2 launch swd_robot_bringup description.launch.py
```
## Launch Simulation
```bash
gz sim
```
## Spawn robot
``` bash
gz service -s /world/<world_name>/create ...
```
## Check Lidar
```bash
gz topic -l | grep lidar
gz topic -e -t /lidar
```