/* -*- c -*- */
/*****************************************************************************/
/*  LibreDWG - free implementation of the DWG file format                    */
/*                                                                           */
/*  Copyright (C) 2019 Free Software Foundation, Inc.                        */
/*                                                                           */
/*  This library is free software, licensed under the terms of the GNU       */
/*  General Public License as published by the Free Software Foundation,     */
/*  either version 3 of the License, or (at your option) any later version.  */
/*  You should have received a copy of the GNU General Public License        */
/*  along with this program.  If not, see <http://www.gnu.org/licenses/>.    */
/*****************************************************************************/

/*
 * summaryinfo.spec: DWG file AcDb::SummaryInfo section specification
 * written by Reini Urban
 */

#include "spec.h"

  SINCE(R_2004) {
    IF_ENCODE_FROM_EARLIER {
      FIELD_VALUE(TDCREATE)   = dwg->header_vars.TDCREATE;
      FIELD_VALUE(TDUPDATE)   = dwg->header_vars.TDUPDATE;
    }
  }

  FIELD_TU (TITLE, 1);
  FIELD_TU (SUBJECT, 1);
  FIELD_TU (AUTHOR, 1);
  FIELD_TU (KEYWORDS, 1);
  FIELD_TU (COMMENTS, 1);
  FIELD_TU (LASTSAVEDBY, 1);
  FIELD_TU (REVISIONNUMBER, 1);
  FIELD_TU (HYPERLINKBASE, 1);
  DEBUG_HERE;
  FIELD_TIMEBLL (total_editing_time, 0);
  FIELD_TIMEBLL (TDCREATE, 0);
  FIELD_TIMEBLL (TDUPDATE, 0);
  FIELD_RS (num_props, 0);
  DEBUG_HERE;
  REPEAT(num_props, props, Dwg_SummaryInfo_Property)
    {
      FIELD_T (props[rcount1].key, 0);
      FIELD_T (props[rcount1].value, 0);
    }
  END_REPEAT(texts)
  DEBUG_HERE;
  FIELD_RL (unknown1, 0);
  FIELD_RL (unknown2, 0);

