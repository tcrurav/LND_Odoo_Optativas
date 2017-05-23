# -*- coding: utf-8 -*-

from odoo import models, fields, api

class curso(models.Model):
    _name = 'optativas.curso'

    name = fields.Char()
    # image: fields.binary("Image",
    #         help="This field holds the image used as image for our customers, limited to 1024x1024px.")
    # 'image_medium': fields.function(_get_image, fnct_inv=_set_image,
    #         string="Image (auto-resized to 128x128):", type="binary", multi="_get_image",
    #         store={
    #             'upload_images.tutorial': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
    #         },help="Medium-sized image of the category. It is automatically "\
    #              "resized as a 128x128px image, with aspect ratio preserved. "\
    #              "Use this field in form views or some kanban views."),
    # 'image_small': fields.function(_get_image, fnct_inv=_set_image,
    #         string="Image (auto-resized to 64x64):", type="binary", multi="_get_image",
    #         store={
    #             'upload_images.tutorial': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
    #         },
    #         help="Small-sized image of the category. It is automatically "\
    #              "resized as a 64x64px image, with aspect ratio preserved. "\
    #              "Use this field anywhere a small image is required.")
    #
    # def _get_image(self, cr, uid, ids, name, args, context=None):
    #     result = dict.fromkeys(ids, False)
    #     for obj in self.browse(cr, uid, ids, context=context):
    #         result[obj.id] = tools.image_get_resized_images(obj.image)
    #     return result
    #
    # def _set_image(self, cr, uid, id, name, value, args, context=None):
    #     return self.write(cr, uid, [id], {'image': tools.image_resize_image_big(value)}, context=context)

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
