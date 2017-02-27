window.Sense = {
    "columns": [],
    "rows": [],
    "selected": {
        "path": {},
        "x": 132,
        "y": 99,
        "width": 20,
        "height": 20,
        "active": false,
        "value": ""
    }
} 


function deselect() {
    window.Sense.selected.active = false;
}


$("html").click(function(){
    if(!$(event.target).closest('.dynamic-table').length) {
        deselect()
    }
})




Vue.component('dynamic-table', {
    template: "#tmpl-dynamic-table",
    data: function() {
        return window.Sense
    }, 
    computed: {
        renderedTable: function() {
            let renderedRows = [];
            for(var r = 0; r < this.rows.length; r++){
                // let row = [];
                let rowspan = 1;
                // Compute rowspan
                for(var c = 0; c < this.columns.length; c++){
                    let columnVal = this.rows[r][this.columns[c]];
                    if(columnVal instanceof Array){
                        if(columnVal.length >= rowspan) {
                            rowspan = columnVal.length + 1;
                        }
                    }
                }
                
                for(var rowId = 0; rowId < rowspan; rowId++) {
                    let currentRow = [];
                    if(rowId === 0){
                        currentRow.push({rowspan: rowspan, value: r + 1, "header": true });
                    }
                    
                    for(var c = 0; c < this.columns.length; c++){
                        let columnName = this.columns[c];
                        let columnVal = this.rows[r][columnName];
                        if(columnVal instanceof Array){
                            if(rowId < columnVal.length){
                                let value = columnVal[rowId]
                                currentRow.push({
                                    "rowspan": 1,
                                    "value": value,
                                    "path": {
                                        "id": r,
                                        columnName: value,
                                        "_next": {
                                            "_index": rowId
                                        },
                                        "_row": "id",
                                        "_col": columnName
                                    }
                                })
                            } else if (rowId === columnVal.length) {
                                currentRow.push({
                                    "rowspan": rowspan - columnVal.length,
                                    "value": "",
                                    "path": {
                                        "id": r,
                                        columnName: "",
                                        "_next": {
                                            "_index": rowId
                                        },
                                        "_row": "id",
                                        "_col": columnName
                                    }
                                })
                            }
                        }
                        else {
                            if(rowId === 0){
                                currentRow.push({
                                    "rowspan": rowspan, 
                                    "value": columnVal,
                                    "path": {
                                        "id": r,
                                        columnName: columnVal,
                                        "_row": "id",
                                        "_col": columnName
                                    }
                                });
                            }
                        }
                    }
                    renderedRows.push(currentRow);
                }
                // renderedRows.push(row);
            }
            return renderedRows;
        }
    },
    methods: {
        addRow: function(){
            let newObject = {};
            for(var i = 0; i < this.columns.length; i++){
                // TODO: Append the appropriate zero value for each row
                newObject[this.columns[i]] = ""
            }
            this.rows.append(newObject)
        },
        setItem: function(path, value) {
            console.log(path);
            // TODO: This should eventually work for infinitely nested objects.
            let row = path["id"];
            let col = path["_col"];
            console.log(path["_next"] !== undefined);
            if (path["_next"] !== undefined){
                let index = path["_next"]["_index"]
                // Have to do it this way to force it to update properly
                var arrClone = this.rows[row][col].slice(0);
                arrClone[index] = value;
                // If you clear out the last value, then the cell goes away
                if (index == arrClone.length -1 && value == "") {
                    arrClone.pop()
                }
                this.rows[row][col] = arrClone;
                
            } else {
                this.rows[row][col] = value;
            }
        },
        saveEdit: function() {
            if(this.selected.active){
                // Save the existing value
                this.setItem(this.selected.path, this.selected.value);
            }
        },
        select: function(col, event) {
            window.evt = event;
            this.saveEdit();
            this.selected.active = true;
            this.selected.x = event.target.offsetLeft;
            this.selected.y = event.target.offsetTop;
            this.selected.width = event.target.offsetWidth;
            this.selected.height = event.target.offsetHeight;
            
            this.selected.path = col.path;
            this.selected.value = col.value;

            $(".CellInput textarea").focus()
        },
        deselect: function(e) {
            this.saveEdit();
            this.selected.active = false;
            e.preventDefault();
            e.stopPropagation();
        },
        selectNextColumn: function(){},
        selectPrevColumn: function(){},
    }
});



var app = new Vue({
    el: '#app',
    methods: { }
});
