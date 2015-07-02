var NavbarView = Backbone.View.extend({

	//  tagName: "gridview",
	  id: "navbarview",

	  className: "navbar-view",

	  initialize: function(newModel) {
		this.listenTo(newModel, "change", this.render);
		this.self = this;
		self.model = newModel;		
	  },

	  render: function(state) {
		// this is set so that the events get triggered correctly.
		this.setElement(jQuery('#'+this.id));		  
		
		/* Detail View */
		if ( state == "detailview" ) {
		// rendering takes place here, based on handlebars templates			
		var i = 0;
		// get the active detail ID (the one we should show, set on click on gridview)
		i = self.model.get("active_detail");		
			var context = {data: self.model.get("data").arr[i], backbutton:true };				
		}
		/* Grid View */
		else {
			var newdata = {};
			newdata.name = "Hub";
			var context = {data: newdata};				
		}	

		var source   = $("#navbarview-template").html();
		var template = Handlebars.compile(source);		
		var html    = template(context);	

		jQuery('#'+this.id).html(html);
		//console.log("rendered" +html);
	  }

	});