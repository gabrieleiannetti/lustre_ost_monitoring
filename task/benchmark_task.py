#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Gabriele Iannetti <g.iannetti@gsi.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import os
import time

from task.base_task import BaseTask


class BenchmarkTask(BaseTask):

    def execute(self):

        pid = os.getpid()
        outfile = f"/tmp/benchmark_task_{pid}.tmp"

        tid_num = int(self.tid)
        waittime = (tid_num % 100 / 1000)
        time.sleep(waittime)

        with open(outfile, "a") as myfile:
            myfile.write(f"TID: {tid_num} - PID: {pid} - Wait: {waittime}\n")
