using AlfaCoreDumped.Domain.Entities.CompanyResources;

namespace AlfaCoreDumped.Infrastructure.DbRepository
{
    public interface IAlfaRepository
    {
        bool Save();
        Area GetArea(Guid areaId);
        void AddArea(Area area);
    }
}
