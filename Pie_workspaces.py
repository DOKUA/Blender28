# -*- coding: utf-8 -*-

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Pie Workspaces",
    "description": "Pie Workspaces",
    "author": "Laurent Laget, Lapineige",
    "version": (0, 1, 4),
    "blender": (2, 80, 1),
    "location": "keyboard",
    "warning": "Press Ctrl Alt W to use the pie.Please add the 2D animation and Masking workspaces manually.",
    "wiki_url": "",
    "category": "3d View"
    }

import bpy
from bpy.types import Menu


# Pie Workspaces - alt right mouse button
class VIEW3D_PIE_workspaces(Menu):
    bl_idname = "pie.workspaces"
    bl_label = "Workspaces"

    def draw(self, context):
        layout = self.layout
        
        #layout.operator_context = 'INVOKE_REGION_WIN'
        pie = layout.menu_pie()
        col = pie.split().column()
        row = col.split(align=True)
 
        col.operator("class.layout", text ="Layout", icon ='SCENE_DATA')
        col = pie.column(align=True)
        
        col.operator("class.modeling", text ="Modeling", icon ='EDITMODE_HLT')
        col = pie.column(align=True)
        
        col.operator("class.worksculpt", text ="Sculpt", icon ='SCULPTMODE_HLT')
        col = pie.column(align=True)
        
        col.operator("class.uvediting", text ="UV Editing", icon ='UV_ISLANDSEL')
        col = pie.column(align=True)
        
        col.operator("class.texturepaint", text ="Texture Paint", icon ='BRUSH_DATA')
        col = pie.column(align=True)
        
        col.operator("class.shading", text ="Shading", icon ='MATERIAL_DATA')
        col = pie.column(align=True)
        
        col.operator("class.animation", text ="3D Animation", icon ='SEQUENCE')
        col.operator("class.da", text ="2D Animation", icon ='GREASEPENCIL')
        col.operator("class.scripting", text ="Scripting", icon ='SCRIPTPLUGINS')
        col = pie.column(align=True)
        
        col.operator("class.rendering", text ="Rendering", icon ='SCENE')
        col.operator("class.compositing", text ="Compositing", icon ='RENDER_RESULT')
        col.operator("class.masking", text ="Masking", icon ='RESTRICT_VIEW_ON')
        col = pie.column(align=True)
        

class layout(bpy.types.Operator):
    bl_idname = "class.layout"
    bl_label = "layout"
    
    def execute(self, context):
        
        layout = self.layout
        bpy.data.window_managers['WinMan'].windows[0].workspace = bpy.data.workspaces['Layout']
        return {'FINISHED'}

class modeling(bpy.types.Operator):
    bl_idname = "class.modeling"
    bl_label = "modeling"
    
    def execute(self, context):
        
        layout = self.layout
        bpy.data.window_managers['WinMan'].windows[0].workspace = bpy.data.workspaces['Modeling']
        return {'FINISHED'}

class worksculpt(bpy.types.Operator):
    bl_idname = "class.worksculpt"
    bl_label = "worksculpt"
    
    def execute(self, context):
        
        layout = self.layout
        bpy.data.window_managers['WinMan'].windows[0].workspace = bpy.data.workspaces['Sculpting']
        return {'FINISHED'}
    
class uvediting(bpy.types.Operator):
    bl_idname = "class.uvediting"
    bl_label = "uvediting"
    
    def execute(self, context):
        
        layout = self.layout
        bpy.data.window_managers['WinMan'].windows[0].workspace = bpy.data.workspaces['UV Editing']
        return {'FINISHED'}
    
class texturepaint(bpy.types.Operator):
    bl_idname = "class.texturepaint"
    bl_label = "texturepaint"
    
    def execute(self, context):
        
        layout = self.layout
        bpy.data.window_managers['WinMan'].windows[0].workspace = bpy.data.workspaces['Texture Paint']
        return {'FINISHED'}

class shading(bpy.types.Operator):
    bl_idname = "class.shading"
    bl_label = "shading"
    
    def execute(self, context):
        
        layout = self.layout
        bpy.data.window_managers['WinMan'].windows[0].workspace = bpy.data.workspaces['Shading']
        return {'FINISHED'}

class animation(bpy.types.Operator):
    bl_idname = "class.animation"
    bl_label = "animation"
    
    def execute(self, context):
        
        layout = self.layout
        bpy.data.window_managers['WinMan'].windows[0].workspace = bpy.data.workspaces['Animation']
        return {'FINISHED'}
    
class rendering(bpy.types.Operator):
    bl_idname = "class.rendering"
    bl_label = "rendering"
    
    def execute(self, context):
        
        layout = self.layout
        bpy.data.window_managers['WinMan'].windows[0].workspace = bpy.data.workspaces['Rendering']
        return {'FINISHED'}
    
class compositing(bpy.types.Operator):
    bl_idname = "class.compositing"
    bl_label = "compositing"
    
    def execute(self, context):
        
        layout = self.layout
        bpy.data.window_managers['WinMan'].windows[0].workspace = bpy.data.workspaces['Compositing']
        return {'FINISHED'}
    

class da(bpy.types.Operator):
    bl_idname = "class.da"
    bl_label = "da"
    
    def execute(self, context):
        
        layout = self.layout
        bpy.data.window_managers['WinMan'].windows[0].workspace = bpy.data.workspaces['2D Animation']
        return {'FINISHED'}
    
    
class scripting(bpy.types.Operator):
    bl_idname = "class.scripting"
    bl_label = "scripting"
    
    def execute(self, context):
        
        layout = self.layout
        bpy.data.window_managers['WinMan'].windows[0].workspace = bpy.data.workspaces['Scripting']
        return {'FINISHED'}

class masking(bpy.types.Operator):
    bl_idname = "class.masking"
    bl_label = "masking"
    
    def execute(self, context):
        
        layout = self.layout
        bpy.data.window_managers['WinMan'].windows[0].workspace = bpy.data.workspaces['Masking']
        return {'FINISHED'}


classes = (
    VIEW3D_PIE_workspaces,
    modeling,
    worksculpt,
    uvediting,
    layout,
    texturepaint,
    shading,
    animation,
    rendering,
    compositing,
    da,
    scripting,
    masking,
    )

addon_keymaps = []


def register():

    for cls in classes:
        bpy.utils.register_class(cls)
    wm = bpy.context.window_manager
    kc = bpy.context.window_manager.keyconfigs.addon
    if wm.keyconfigs.addon:
        
        km = wm.keyconfigs.addon.keymaps.new(name = "Window",space_type='EMPTY', region_type='WINDOW')
 
        kmi = km.keymap_items.new('wm.call_menu_pie', 'W', 'PRESS' ,alt=True,ctrl=True)
        kmi.properties.name = "pie.workspaces"
        addon_keymaps.append((km,kmi))

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
