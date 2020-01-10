/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 8; tab-width: 8 -*- */
/* gkr-misc.h - miscellaneous utilities

   Copyright (C) 2009 Stefan Walter

   The Gnome Keyring Library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Library General Public License as
   published by the Free Software Foundation; either version 2 of the
   License, or (at your option) any later version.

   The Gnome Keyring Library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Library General Public License for more details.

   You should have received a copy of the GNU Library General Public
   License along with the Gnome Library; see the file COPYING.LIB.  If not,
   write to the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
   Boston, MA 02111-1307, USA.

   Author: Stef Walter <stef@memberwebs.com>
*/

#ifndef GKR_MISC_H
#define GKR_MISC_H

#include "gnome-keyring.h"

#include <glib.h>

extern const gchar *    gkr_service_name;

gchar*                  gkr_encode_keyring_name              (const gchar *keyring);

gchar*                  gkr_encode_keyring_item_id           (const gchar *keyring,
                                                              guint32 id);

gchar*                  gkr_decode_keyring_name              (const char *path);

gboolean                gkr_decode_item_id                   (const char *path,
                                                              guint32 *id);

gchar*                  gkr_decode_keyring_item_id           (const char *path,
                                                              guint32* id);

gboolean                gkr_decode_is_keyring                (const char *path);

gchar *                 gkr_attributes_print                 (GnomeKeyringAttributeList *attrs);

#endif /* GKR_MISC_H */
