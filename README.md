# SWD Robot Autonomous SLAM (ROS 2)

This repository contains a full pipeline for autonomous SLAM and navigation using a mobile robot.

##  Overview

The project is structured to support:

- Simulation (Gazebo Harmonic + ROS 2 Jazzy)
- Real robot deployment (ROS 2 Humble)
- Clean separation between:
  - robot description
  - simulation
  - SLAM
  - navigation
  - experiments

---

## Workspace Structure
ws_ros2/
├── src/
│ ├── swd_starter_kit_description/
│ ├── swd_robot_bringup/
│ ├── swd_robot_gazebo/
│ ├── swd_robot_slam/
│ ├── swd_robot_navigation/
│ └── swd_robot_experiments/

---

##  Setup

See: `docs/setup.md`

---

##  Simulation

See: `docs/usage.md`

---

##  Notes

- Simulation uses ROS 2 Jazzy
- Real robot uses ROS 2 Humble
- Config files are separated per distro

---

##  TODO

- [ ] Lidar working in Gazebo
- [ ] Bridge Gazebo → ROS 2
- [ ] SLAM Toolbox integration
- [ ] Nav2 integration