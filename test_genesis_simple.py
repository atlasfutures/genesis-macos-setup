import genesis as gs

def main():
    # Initialize Genesis with CPU backend
    gs.init(backend=gs.cpu)

    # Create a scene without visualization
    scene = gs.Scene(
        sim_options=gs.options.SimOptions(),
        show_viewer=False,
        rigid_options=gs.options.RigidOptions(
            dt=0.01,
            gravity=(0.0, 0.0, -10.0),
        ),
    )

    # Add a plane and a Franka robot
    plane = scene.add_entity(gs.morphs.Plane())
    robot = scene.add_entity(
        gs.morphs.MJCF(file="Genesis/genesis/assets/xml/franka_emika_panda/panda.xml"),
    )

    # Build the scene
    scene.build()

    # Run simulation for a few steps
    print("\nStarting simulation...")
    for i in range(10):
        scene.step()
        if i % 2 == 0:
            print(f"\nStep {i}:")
            print("Robot position:", robot.get_pos())
            print("Robot orientation:", robot.get_quat())
            print("Robot joint positions:", robot.get_dofs_position())
            print("Robot joint velocities:", robot.get_dofs_velocity())

if __name__ == "__main__":
    main()
