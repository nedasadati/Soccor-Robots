from controller import Robot,Receiver, DistanceSensor, Motor, Compass, PositionSensor
import struct
import math

TIME_STEP = 64
robot = Robot()
name=robot.getName()
team=name[0]
player=name[1]
my_res = robot.getReceiver('receiver')
my_res.enable(5)

compass = robot.getCompass('compass')
compass.enable(5)

pos = robot.getPositionSensor('pos')
pos.enable(5)

leftMotor  = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')
m_pos = robot.getMotor('m_pos')

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
m_pos.setPosition(float('inf'))

leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)
m_pos.setVelocity(0)

def kicker(v_pos1, state):
    shoot = 0
    if v_pos1>-0.8 and v_pos1<=0 and state ==1:
        shoot = -10
    elif dxz> 0.2 and v_pos1<-0.01:
        shoot = 10
    return shoot
    
    
leftSpeed  = 0
rightSpeed = 0

while robot.step(TIME_STEP) != -1:
    shoot =0
    compass_data = compass.getValues()
    
    zavie1 = math.atan2(compass_data[0], compass_data[2])
    bearing = (zavie1 - 1.5708) / math.pi * 180.0
    if (bearing < 0.0):
        bearing = bearing + 360.0
            
    x=my_res.getQueueLength()
    if x:
        d=my_res.getData()
        dataList=struct.unpack("dddddddddddddddddddd",d)
        
        if player=='1':
            rx=dataList[9]
            rz=dataList[10]
        if player=='2':
            rx=dataList[12]
            rz=dataList[13]
        if player=='3':
            rx=dataList[15]
            rz=dataList[16]
        bx=dataList[18]
        bz=dataList[19]
     

        if player=='1':
        
            leftSpeed  = -4
            rightSpeed = 4
            
            dx=rx-bx
            dz=rz-bz
            dxz=math.sqrt(dx**2+dz**2)
            
            
            state=0  
            v_pos=pos.getValue()        
            shoot = kicker(v_pos, state) 
             
                
            holder1 = math.atan2(dz, dx)
            h1 = holder1 * 180.0 / math.pi
            dis=bearing-h1
                
            if dis>82.0 and dis<94.0 or dis>437.0 and dis<449.0:
                    
                leftSpeed=-7
                rightSpeed=-7
               
                if dxz<0.080:
                    state=1
                    v_pos=pos.getValue() 
                    shoot = kicker(v_pos , state)
                    
                          
        elif player=='2':
            leftSpeed=3
            rightSpeed=-3
            
            dx=rx-bx
            dz=rz-bz
            dxz=math.sqrt(dx**2+dz**2)

            state=0  
            v_pos=pos.getValue()        
            shoot = kicker(v_pos, state) 
                
            holder1 = math.atan2(dz, dx)
            h1 = holder1 * 180.0 / math.pi
                
            dis=bearing-h1
           
                
            if dis>87.0 and dis<97.0 or dis>447.0 and dis<455.0:
                    
                leftSpeed=-6
                rightSpeed=-6
               
                if dxz<0.096:
                    state=1
                    v_pos=pos.getValue() 
                    shoot = kicker(v_pos , state)
                
 
            
        elif player=='3':
            dx=rx+bx
            dz=rz+bz
            dxz=math.sqrt(dx**2+dz**2)
            
            state=0  
            v_pos=pos.getValue()        
            shoot = kicker(v_pos , state)
            
            leftSpeed=1
            rightSpeed=1
            
            if rz>bz:
                leftSpeed= 6
                rightSpeed= 6
            else:
                leftSpeed=-6
                rightSpeed=-6
                
            if dxz<0.096:
                
                state=1
                v_pos=pos.getValue() 
                shoot = kicker(v_pos , state)

                         
        my_res.nextPacket() 
        m_pos.setVelocity(shoot)
        leftMotor.setVelocity(leftSpeed)
        rightMotor.setVelocity(rightSpeed)
    
      

