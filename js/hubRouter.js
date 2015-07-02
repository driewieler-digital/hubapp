		// set up the router
		var hubRouter = Backbone.Router.extend({
		
		initialize: function(model1, navbar1){
			this.self = this;
			self.navbar = navbar1;	
			self.model = model1;
		},
		
		  routes: {
			"": 			   "gridview",	// no address => to gridview			
			"gridview":        "gridview",
			"detail/:id": 	   "detail", 
			"settings":        "settings",			
		  },

		  settings: function() {
			// show the settings view
			console.log("Showing settings view");
		  },

		  gridview: function() {
			// show the gridview
			console.log("Showing grid view");
			
			jQuery('#gridview').css('display', 'block');
			jQuery('#detailview').css('display', 'none');			
			self.navbar.render('gridview');			
		  },		

		  detail: function(id) {
			// show the detailview for specified id
			console.log("Showing detail view for #"+id);
		
			self.model.set("active_detail", id-1);		
			
			jQuery('#gridview').css('display', 'none');
			jQuery('#detailview').css('display', 'block');
			self.navbar.render('detailview');			
			}
		  
		
		});