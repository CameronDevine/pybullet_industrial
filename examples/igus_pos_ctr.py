import os
import time
import pybullet as p
import wbk_sim as wbk
import rolap

if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    parentDir = os.path.dirname(dirname)
    urdf_file1 = os.path.join( parentDir,'src','wbk_sim','robot_descriptions', 'igus_4DOF_SV.urdf')

    physics_client = p.connect(p.GUI)
    p.setPhysicsEngineParameter(numSolverIterations=1000)
    start_orientation = p.getQuaternionFromEuler([0, 0, 0])
    robot = wbk.RobotBase(urdf_file1,[0,0,0],start_orientation)

    

    p.setRealTimeSimulation(1)

    target_position = [0.-0.05, 0.3]
    test_path = rolap.build_lemniscate_path(target_position,400,0,0.3)
    wbk.draw_path(test_path)
    for i in range(400): 
        target_orientation = p.getQuaternionFromEuler([0, 0, 0]) 
        robot.set_endeffector_pose('link4',test_path[:,i]) 
        time.sleep(0.05) 