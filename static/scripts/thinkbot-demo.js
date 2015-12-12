window.onload = function() {

    var r = new X.renderer3D();
    r.container = 'visualization';
    r.init();
    r.interactor.config.MOUSEWHEEL_ENABLED = false;
    r.interactor.init();

    var solution = new X.mesh();
    solution.file = '/images/projects/thinkbot/elasticity000000.vtk';
    solution.magicmode = true;
    solution.color = [0.5, 0.5, 0.5];
    solution.opacity = 0.85;
  //  solution.color = [0.8, 0.3, 0.3];
//    solution.opacity = 0.6;
    r.add(solution);

    // For elasticity
    r.camera.position = [0, 0, 35];
    r.camera.focus = [0, 0, 0];

    // For gear
//    r.camera.position = [0, 0, 1.55];
//    r.camera.focus = [0, 0, 0];

    // For hyperelasticity
    // r.camera.position = [0, 0, 2];
    // r.camera.focus = [0, 0, 0];

    // animate..
    r.onRender = function() {

	solution.transform.rotateY(0.4);

	// we could also rotate the camera instead which is better in case
	// we have a lot of objects and want to rotate them all:
	//
	// r.camera.rotate([1,0]);

    };

    r.render();

};
