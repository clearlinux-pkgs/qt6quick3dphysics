#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
Name     : qt6quick3dphysics
Version  : 6.6.1
Release  : 5
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.1/submodules/qtquick3dphysics-everywhere-src-6.6.1.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.1/submodules/qtquick3dphysics-everywhere-src-6.6.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-3.0
Requires: qt6quick3dphysics-lib = %{version}-%{release}
Requires: qt6quick3dphysics-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
BuildRequires : qt6quick3d-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Qt Quick 3D Physics
Qt Quick 3D Physics provides a high-level API for physics simulation. It supports simulating interactive rigid bodies as well as static meshes and non-colliding bodies used for detecting overlaps. Every simulated body can have its own physical properties like mass, density and friction.

%package dev
Summary: dev components for the qt6quick3dphysics package.
Group: Development
Requires: qt6quick3dphysics-lib = %{version}-%{release}
Provides: qt6quick3dphysics-devel = %{version}-%{release}
Requires: qt6quick3dphysics = %{version}-%{release}

%description dev
dev components for the qt6quick3dphysics package.


%package lib
Summary: lib components for the qt6quick3dphysics package.
Group: Libraries
Requires: qt6quick3dphysics-license = %{version}-%{release}

%description lib
lib components for the qt6quick3dphysics package.


%package license
Summary: license components for the qt6quick3dphysics package.
Group: Default

%description license
license components for the qt6quick3dphysics package.


%prep
%setup -q -n qtquick3dphysics-everywhere-src-6.6.1
cd %{_builddir}/qtquick3dphysics-everywhere-src-6.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703023737
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1703023737
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6quick3dphysics
cp %{_builddir}/qtquick3dphysics-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6quick3dphysics/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtquick3dphysics-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6quick3dphysics/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtquick3dphysics-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6quick3dphysics/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtquick3dphysics-everywhere-src-%{version}/src/3rdparty/PhysX/LICENSE.md %{buildroot}/usr/share/package-licenses/qt6quick3dphysics/f2364c0bf726617dbc7875838259608e8c1a8fb6 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/bin/cooker
/usr/lib64/qt6/metatypes/qt6quick3dphysics_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6quick3dphysicshelpers_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/modules/qt_lib_quick3dphysics.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_quick3dphysics_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_quick3dphysicshelpers.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_quick3dphysicshelpers_private.pri
/usr/lib64/qt6/modules/Quick3DPhysics.json
/usr/lib64/qt6/modules/Quick3DPhysicsHelpers.json
/usr/lib64/qt6/qml/QtQuick3D/Physics/Helpers/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick3D/Physics/Helpers/qmldir
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/BoxShapeSection.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/BoxShapeSpecifics.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/CapsuleShapeSection.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/CapsuleShapeSpecifics.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/CharacterControllerSection.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/CharacterControllerSpecifics.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/CollisionShapeSection.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/ConvexMeshShapeSection.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/ConvexMeshShapeSpecifics.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/DynamicRigidBodySection.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/DynamicRigidBodySpecifics.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/HeightFieldShapeSection.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/HeightFieldShapeSpecifics.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/NodeSection.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/PhysicsBodySection.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/PhysicsMaterialSection.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/PhysicsMaterialSpecifics.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/PhysicsNodeSection.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/PhysicsWorldSection.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/PhysicsWorldSpecifics.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/PlaneShapeSpecifics.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/SphereShapeSection.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/SphereShapeSpecifics.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/StaticRigidBodySpecifics.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/TriangleMeshShapeSection.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/TriangleMeshShapeSpecifics.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/TriggerBodySpecifics.qml
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/boxshape.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/boxshape16.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/boxshape@2x.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/capsuleshape.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/capsuleshape16.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/capsuleshape@2x.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/charactercontroller.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/charactercontroller16.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/charactercontroller@2x.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/convexmeshshape.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/convexmeshshape16.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/convexmeshshape@2x.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/dynamicrigidbody.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/dynamicrigidbody16.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/dynamicrigidbody@2x.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/heightfieldshape.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/heightfieldshape16.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/heightfieldshape@2x.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/physicsmaterial.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/physicsmaterial16.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/physicsmaterial@2x.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/physicsworld.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/physicsworld16.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/physicsworld@2x.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/planeshape.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/planeshape16.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/planeshape@2x.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/sphereshape.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/sphereshape16.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/sphereshape@2x.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/staticrigidbody.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/staticrigidbody16.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/staticrigidbody@2x.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/trianglemeshshape.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/trianglemeshshape16.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/trianglemeshshape@2x.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/triggerbody.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/triggerbody16.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/images/triggerbody@2x.png
/usr/lib64/qt6/qml/QtQuick3D/Physics/designer/physics.metainfo
/usr/lib64/qt6/qml/QtQuick3D/Physics/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick3D/Physics/qmldir

%files dev
%defattr(-,root,root,-)
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qabstractcollisionshape_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qabstractphysicsbody_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qabstractphysicsnode_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qabstractphysxnode_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qboxshape_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qcacheutils_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qcapsuleshape_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qcharactercontroller_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qcollisiondebugmeshbuilder_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qconvexmeshshape_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qdebugdrawhelper_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qdynamicrigidbody_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qheightfieldshape_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qphysicscommands_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qphysicsmaterial_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qphysicsmeshutils_p_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qphysicsutils_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qphysicsworld_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qphysxactorbody_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qphysxcharactercontroller_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qphysxdynamicbody_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qphysxrigidbody_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qphysxstaticbody_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qphysxtriggerbody_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qphysxworld_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qplaneshape_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qsphereshape_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qstaticphysxobjects_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qstaticrigidbody_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qtrianglemeshshape_p.h
/usr/include/QtQuick3DPhysics/6.6.1/QtQuick3DPhysics/private/qtriggerbody_p.h
/usr/include/QtQuick3DPhysics/QtQuick3DPhysics
/usr/include/QtQuick3DPhysics/QtQuick3DPhysicsDepends
/usr/include/QtQuick3DPhysics/QtQuick3DPhysicsVersion
/usr/include/QtQuick3DPhysics/qtquick3dphysicsglobal.h
/usr/include/QtQuick3DPhysics/qtquick3dphysicsversion.h
/usr/include/QtQuick3DPhysicsHelpers/6.6.1/QtQuick3DPhysicsHelpers/private/qcapsulegeometry_p.h
/usr/include/QtQuick3DPhysicsHelpers/QtQuick3DPhysicsHelpers
/usr/include/QtQuick3DPhysicsHelpers/QtQuick3DPhysicsHelpersDepends
/usr/include/QtQuick3DPhysicsHelpers/QtQuick3DPhysicsHelpersVersion
/usr/include/QtQuick3DPhysicsHelpers/qtquick3dphysicshelpersversion.h
/usr/lib64/cmake/Qt6/FindWrapBundledPhysXConfigExtra.cmake
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtQuick3DPhysicsTestsConfig.cmake
/usr/lib64/cmake/Qt6BundledPhysX/Qt6BundledPhysXAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6BundledPhysX/Qt6BundledPhysXConfig.cmake
/usr/lib64/cmake/Qt6BundledPhysX/Qt6BundledPhysXConfigVersion.cmake
/usr/lib64/cmake/Qt6BundledPhysX/Qt6BundledPhysXConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6BundledPhysX/Qt6BundledPhysXTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6BundledPhysX/Qt6BundledPhysXTargets.cmake
/usr/lib64/cmake/Qt6BundledPhysX/Qt6BundledPhysXVersionlessTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qquick3dphysicspluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qquick3dphysicspluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qquick3dphysicspluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qquick3dphysicspluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qquick3dphysicspluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qquick3dphysicspluginTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquick3dphysicshelperspluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquick3dphysicshelperspluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquick3dphysicshelperspluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquick3dphysicshelperspluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquick3dphysicshelperspluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquick3dphysicshelperspluginTargets.cmake
/usr/lib64/cmake/Qt6Quick3DPhysics/Qt6Quick3DPhysicsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Quick3DPhysics/Qt6Quick3DPhysicsConfig.cmake
/usr/lib64/cmake/Qt6Quick3DPhysics/Qt6Quick3DPhysicsConfigVersion.cmake
/usr/lib64/cmake/Qt6Quick3DPhysics/Qt6Quick3DPhysicsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Quick3DPhysics/Qt6Quick3DPhysicsDependencies.cmake
/usr/lib64/cmake/Qt6Quick3DPhysics/Qt6Quick3DPhysicsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Quick3DPhysics/Qt6Quick3DPhysicsTargets.cmake
/usr/lib64/cmake/Qt6Quick3DPhysics/Qt6Quick3DPhysicsVersionlessTargets.cmake
/usr/lib64/cmake/Qt6Quick3DPhysicsHelpers/Qt6Quick3DPhysicsHelpersAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Quick3DPhysicsHelpers/Qt6Quick3DPhysicsHelpersConfig.cmake
/usr/lib64/cmake/Qt6Quick3DPhysicsHelpers/Qt6Quick3DPhysicsHelpersConfigVersion.cmake
/usr/lib64/cmake/Qt6Quick3DPhysicsHelpers/Qt6Quick3DPhysicsHelpersConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Quick3DPhysicsHelpers/Qt6Quick3DPhysicsHelpersDependencies.cmake
/usr/lib64/cmake/Qt6Quick3DPhysicsHelpers/Qt6Quick3DPhysicsHelpersTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Quick3DPhysicsHelpers/Qt6Quick3DPhysicsHelpersTargets.cmake
/usr/lib64/cmake/Qt6Quick3DPhysicsHelpers/Qt6Quick3DPhysicsHelpersVersionlessTargets.cmake
/usr/lib64/libQt6Quick3DPhysics.prl
/usr/lib64/libQt6Quick3DPhysics.so
/usr/lib64/libQt6Quick3DPhysicsHelpers.prl
/usr/lib64/libQt6Quick3DPhysicsHelpers.so
/usr/lib64/pkgconfig/Qt6Quick3DPhysics.pc
/usr/lib64/pkgconfig/Qt6Quick3DPhysicsHelpers.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt6Quick3DPhysics.so.6
/usr/lib64/libQt6Quick3DPhysics.so.6.6.1
/usr/lib64/libQt6Quick3DPhysicsHelpers.so.6
/usr/lib64/libQt6Quick3DPhysicsHelpers.so.6.6.1
/usr/lib64/qt6/qml/QtQuick3D/Physics/Helpers/libqtquick3dphysicshelpersplugin.so
/usr/lib64/qt6/qml/QtQuick3D/Physics/libqquick3dphysicsplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6quick3dphysics/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6quick3dphysics/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6quick3dphysics/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt6quick3dphysics/f2364c0bf726617dbc7875838259608e8c1a8fb6
