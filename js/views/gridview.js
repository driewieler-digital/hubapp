var GridView = Backbone.View.extend({

	//  tagName: "gridview",
	  id: "gridview",

	  className: "grid-view",
	
	  events: {
		"click .row":          "itemtouched",
	  },

	  initialize: function(newModel) {
		this.listenTo(newModel, "change", this.render);
		this.model = newModel;
	  },

	  render: function(newModel) {
		// this is set so that the events get triggered correctly.
		this.setElement(jQuery('#'+this.id));		  
		// update our reference to the model
		this.model = newModel;		
		
		// rendering takes place here, based on handlebars templates			
		// returns HTML source
		var source   = $("#gridview-template").html();
		var template = Handlebars.compile(source);	
		var context = {data: newModel.get("data") };			
		var html    = template(context);		

		jQuery('#'+this.id).html(html);

	  },
	  
	itemtouched: function(event) {
		console.log("Touched item #" + event.target.id);
	  }

	});
