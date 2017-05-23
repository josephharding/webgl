
Grid.prototype._vao;
Grid.prototype._positions;
Grid.prototype._uvs;

function Grid(sec_width, sec_height, width, height, uvs, gl, posAttrLoc, uvAttrLoc) {

  this._uvs = uvs;
 	this._positions = [];
	for(var i = 0; i < width; i++) {
		for(var j = 0; j < height; j++) {
			var origin_x = i * sec_width;
			var origin_y = j * sec_height;	
			this._positions = this._positions.concat([origin_x, origin_y]);
			this._positions = this._positions.concat([origin_x + sec_width, origin_y]);
			this._positions = this._positions.concat([origin_x + sec_width, origin_y + sec_height]);
			this._positions = this._positions.concat([origin_x + sec_width, origin_y + sec_height]);
			this._positions = this._positions.concat([origin_x, origin_y + sec_height]);
			this._positions = this._positions.concat([origin_x, origin_y]);
    }
	}
 
	this._vao = gl.createVertexArray();
	gl.bindVertexArray(this._vao);
	
  var positionBuffer = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(this._positions), gl.STATIC_DRAW);
  gl.enableVertexAttribArray(posAttrLoc);
  gl.vertexAttribPointer(posAttrLoc, 2, gl.FLOAT, false, 0, 0);
  
  var uvBuffer = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, uvBuffer);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(this._uvs), gl.STATIC_DRAW);
  gl.enableVertexAttribArray(uvAttrLoc);
  gl.vertexAttribPointer(uvAttrLoc, 2, gl.FLOAT, false, 0, 0);
}

Grid.prototype.draw = function(gl) {
	gl.bindVertexArray(this._vao);
  gl.drawArrays(gl.TRIANGLES, 0, this._positions.length / 2);
};
