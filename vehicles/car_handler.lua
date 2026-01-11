-- car_handler.lua
-- yes its lua, dont mind me LOL asfkeqfqpfojqpof

local function car_handler(car_physics_state)
    if car_physics_state == 1 then
        print("handling car....")
        print("getting ready to initialize car physics...")
        print("changing the state of car physics to 1...")
        print("car physics state is: ", car_physics_state)
        print("finished car handling!")
    else
        print("car physics state is 0!")
    end
end

car_handler(1)
