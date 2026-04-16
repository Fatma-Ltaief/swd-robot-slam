# Setup Guide

## Requirements

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo Harmonic

## Install ROS 2

Follow official instructions:
https://docs.ros.org/en/jazzy/

## Install dependencies

```bash
sudo apt update
sudo apt install -y \
  ros-jazzy-nav2-bringup \
  ros-jazzy-slam-toolbox \
  ros-jazzy-ros-gz
```

## Install dependencies

```bash
cd ~/ws_ros2
colcon build --symlink-install
source install/setup.bash
```

# Step 5 — Usage guide

Create `docs/usage.md`:

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
# Step 6 — Architecture doc

Create `docs/architecture.md`:

```markdown
# Architecture

## Layers

### 1. Description
- URDF / meshes
- robot_state_publisher

### 2. Simulation
- Gazebo world
- sensors
- physics

### 3. SLAM
- slam_toolbox
- map generation

### 4. Navigation
- Nav2 stack
- planners
- controllers

### 5. Experiments
- RF-aware mapping
- multi-robot coordination


