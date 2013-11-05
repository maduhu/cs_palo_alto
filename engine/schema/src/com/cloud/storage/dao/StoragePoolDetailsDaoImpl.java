// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.
package com.cloud.storage.dao;

import javax.ejb.Local;

import org.apache.cloudstack.framework.config.ConfigKey;
import org.apache.cloudstack.framework.config.ConfigKey.Scope;
import org.apache.cloudstack.framework.config.ScopedConfigStorage;
import org.apache.cloudstack.resourcedetail.ResourceDetailsDaoBase;
import org.apache.cloudstack.storage.datastore.db.StoragePoolDetailVO;
import org.apache.cloudstack.storage.datastore.db.StoragePoolDetailsDao;


@Local(value = StoragePoolDetailsDao.class)
public class StoragePoolDetailsDaoImpl extends ResourceDetailsDaoBase<StoragePoolDetailVO> implements StoragePoolDetailsDao, ScopedConfigStorage {

    public StoragePoolDetailsDaoImpl() {
    }

    @Override
    public Scope getScope() {
        return ConfigKey.Scope.StoragePool;
    }

    @Override
    public String getConfigValue(long id, ConfigKey<?> key) {
        StoragePoolDetailVO vo = findDetail(id, key.key());
        return vo == null ? null : vo.getValue();
    }

    @Override
    public void addDetail(long resourceId, String key, String value) {
        super.addDetail(new StoragePoolDetailVO(resourceId, key, value));
    }
}
