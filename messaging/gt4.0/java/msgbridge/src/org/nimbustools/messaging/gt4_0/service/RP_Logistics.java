/*
 * Copyright 1999-2008 University of Chicago
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy
 * of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 */

package org.nimbustools.messaging.gt4_0.service;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.nimbustools.messaging.gt4_0.common.Constants_GT4_0;
import org.nimbustools.messaging.gt4_0.BasicRP;

public class RP_Logistics extends BasicRP {

    // -------------------------------------------------------------------------
    // STATIC VARIABLES
    // -------------------------------------------------------------------------

    protected static final Log logger =
            LogFactory.getLog(RP_Logistics.class.getName());


    // -------------------------------------------------------------------------
    // INSTANCE VARIABLES
    // -------------------------------------------------------------------------

    protected final InstanceResource rsrc;

    
    // -------------------------------------------------------------------------
    // CONSTRUCTOR
    // -------------------------------------------------------------------------

    public RP_Logistics(InstanceResource resource) {
        super(Constants_GT4_0.RP_LOGISTICS);
        if (resource == null) {
            throw new IllegalArgumentException("resource may not be null");
        }
        this.rsrc = resource;
    }


    // -------------------------------------------------------------------------
    // extends BasicRP
    // -------------------------------------------------------------------------

    public Object getValue() {
        return this.rsrc.getLogistics();
    }

    public void setValue(Object value) {
        logger.warn("Does nothing.");
    }
}
