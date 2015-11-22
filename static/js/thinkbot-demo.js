window.onload = function() {

    var r = new X.renderer3D();
    r.container = 'visualization';
    r.init();

    var solution = new X.mesh();
    solution.file = '/img/projects/thinkbot/elasticity000000.vtk';
    //solution.magicmode = true;
    solution.color = [0.2, 0.2, 0.4];
    solution.opacity = 0.9;
  //  solution.color = [0.8, 0.3, 0.3];
//    solution.opacity = 0.6;
    r.add(solution);

    // For elasticity
    r.camera.position = [0, 0, 40];
    r.camera.focus = [0, 0, 0];

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
