/* Main controller */

var app = {

	initialize: function(){

		var server = Config.get("server");

		/* Converts JSON from server into a model */
		jQuery.getJSON( server + "/test.json", function( data ) {
	
			// define the model
			var newModel = new Backbone.Model;
			var gridView = new GridView(newModel);		
			var detailView = new DetailView(newModel);
			var navbarView = new NavbarView(newModel);
		
			// define the callback on data changed.
			// empty right now, instead, the views use listeners on the model (so the model stays unaware of the views)
			  newModel.on('change:data', function(model, data) {
			  console.log("data changed");
			});
		
			// store the received data, which will trigger the render callback for the first time
			newModel.set('data', data);		
		
			var router = new hubRouter(newModel, navbarView);
			// initialize router
			Backbone.history.start();		

		});

	}

}