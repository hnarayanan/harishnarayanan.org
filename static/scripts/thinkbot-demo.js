window.onload = function() {

    // create and initialize a 3D renderer
    var r = new X.renderer3D();
    r.container = 'visualization';
    r.init();

    // create a new X.mesh
    var skull = new X.mesh();
    // .. and associate the .vtk file to it
    skull.file = '/img/projects/thinkbot/skull.vtk';
    // .. make it transparent
    skull.opacity = 1;
    skull.magicmode = true;
    // .. add the mesh
    r.add(skull);

    // re-position the camera to face the skull
    r.camera.position = [0, 250, 0];

    // animate..
    r.onRender = function() {

	// rotate the skull around the Z axis
	// since we moved the camera, it is Z not X
	skull.transform.rotateZ(1);

	// we could also rotate the camera instead which is better in case
	// we have a lot of objects and want to rotate them all:
	//
	// r.camera.rotate([1,0]);

    };

    r.render();

};
