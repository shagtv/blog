#!/usr/bin/env python
# -*- coding: utf-8 -*-

from OpenGL.GL import *
import time


class ObjLoader:
    def display(self):
        glCallList(self.list)
    
    def __init__(self, filename):
        
        starttime = time.time()
        vertices = []
        normals = []
        texcoords = []
        faces = []
        
        for line in open(filename, "r"):
            values = line.split()
            if not values:
                continue
            elif values[0].startswith("#"):
                continue
            elif values[0] == "v":
                vertices.append([float(x) for x in values[1:4]])
            elif values[0] == "vn":
                normals.append([float(x) for x in values[1:4]])
            elif values[0] == "vt":
                texcoords.append([float(x) for x in values[1:4]])
            elif values[0] == "f":
                face = []
                for elem in values[1:]:
                    face.append([int(x) - 1 for x in elem.split("/")])
                faces.append(face)
        
        avnorms = []
        
        for i in range(len(vertices)):
            avnorms.append([])
            
        for elem in faces:
            for (v, t, n) in elem:
                avnorms[v].append(normals[n])
        
        for i in range(len(avnorms)):
            x, y, z = 0.0, 0.0, 0.0
            num = float(len(avnorms[i]))
            
            if num:
                for value in avnorms[i]:
                    x += value[0]
                    y += value[1]
                    z += value[2]
                avnorms[i] = (x / num, y / num, z / num)
            else:
                avnorms[i] = (0, 0, 1)
        
        self.list = glGenLists(1)
        
        glNewList(self.list, GL_COMPILE)
        glBegin(GL_TRIANGLES)
        
        for face in faces:
            for (vi, ti, ni) in face:
                glNormal3fv(avnorms[vi])
                glTexCoord2fv(texcoords[ti])
                glVertex3fv(vertices[vi])
        
        glEnd()
        glEndList()
        
        print('loading "%s" (%.1fms)' % (filename, (time.time() - starttime) * 1000.0))
