
bl_info = {
    "name": "Joe Mesh Export",
    "description": "mesh exporter",
    "author": "Joe Harding",
    "version": (1, 0),
    "blender": (2, 69, 0),
    "location": "File > Export",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"}

import bpy
import bmesh
import io
import os
import pprint
import mathutils

from bpy_extras.io_utils import ExportHelper


class JoeMesh(bpy.types.Operator, ExportHelper):

    filename_ext = ".json"

    bl_idname = "io.export_mesh"
    # unique identifier for buttons and menu items to reference.

    bl_label = "Mesh Export"
    # display name in the interface.

    bl_options = {'REGISTER', 'UNDO'}
    # enable undo for the operator.

    # execute() is called by blender when running the operator.
    def execute(self, context):
        print("### Mesh Export Script Start ###")

        verts = []
        for poly in bpy.data.meshes['Cube'].polygons:
            for vert_index in poly.vertices:
                verts.append(bpy.data.meshes['Cube'].vertices[vert_index].co)

        print("### Mesh Export Script End ###")
        
        self.write_file(verts) 
        # this lets blender know the operator finished successfully. 
        return {'FINISHED'}


    # print out the mesh data to petgame xml
    def write_file(self, verts):
        filepath = self.filepath
        filepath = bpy.path.ensure_ext(filepath, self.filename_ext)

        print("Exporting to file \"%s\"..." % filepath)

        file = open(filepath, "w")
        fw = file.write

        fw('[')
        for i, val in enumerate(verts):
            fw('{x},{y},{z}'.format(x=val.x, y=val.y, z=val.z))
            if i < len(verts) - 1:
                fw(',\n')

        fw(']')
        file.close()


    def invoke(self, context, event):
        wm = context.window_manager

        if True:
            # File selector
            wm.fileselect_add(self) # will run self.execute()
            return {'RUNNING_MODAL'}
        elif True:
            # search the enum
            wm.invoke_search_popup(self)
            return {'RUNNING_MODAL'}
        elif False:
            # Redo popup
            return wm.invoke_props_popup(self, event)
        elif False:
            return self.execute(context)


def menu_func_export(self, context):
    self.layout.operator(JoeMesh.bl_idname, text="Joe Mesh")


def register():
    bpy.utils.register_class(JoeMesh)
    bpy.types.INFO_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(JoeMesh)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == '__main__':
    register()
