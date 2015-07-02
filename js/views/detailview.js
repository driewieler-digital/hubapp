var DetailView = Backbone.View.extend({

	//  tagName: "gridview",
	  id: "detailview",

	  className: "detail-view",

	  initialize: function(newModel) {
		this.listenTo(newModel, "change", this.render);
	  },

	  render: function(newModel) {
		// this is set so that the events get triggered correctly.
		this.setElement(jQuery('#'+this.id));		  
		
		// rendering takes place here, based on handlebars templates			
		// renders the view from the template.
		// returns HTML source
		var i = 0;
		// get the active detail ID (the one we should show, set on click on gridview)
		i = newModel.get("active_detail");
		var source   = $("#detailview-template").html();
		var template = Handlebars.compile(source);	
		var context = {data: newModel.get("data").arr[i] };					
		var html    = template(context);		

		jQuery('#'+this.id).html(html);
		//console.log("rendered" +html);
	  }

	});
